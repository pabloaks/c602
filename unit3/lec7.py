#!/usr/bin/env python3

import matplotlib.pyplot as plt
import random
import numpy as np

class FairRoulette(object):
    def __init__(self):
        self.pockets = [i for i in range(1,37)]
        self.ball = None
        self.blackOdds, self.redOdds = 1.0, 1.0
        self.pocketOdds = len(self.pockets) - 1.0
    def spin(self):
        self.ball = random.choice(self.pockets)
    def isBlack(self):
        if type(self.ball) != int:
            return False
        if ((self.ball > 0 and self.ball <= 10) \
            or (self.ball > 18 and self.ball <= 28)):
            return self.ball%2 == 0
        else:
            return self.ball%2 == 1
    def isRed(self):
        return type(self.ball) == int and not self.isBlack()
    def betBlack(self, amt):
        if self.isBlack():
            return amt*self.blackOdds
        else:
            return -amt
    def betRed(self, amt):
        if self.isRed():
            return amt*self.redOdds
        else:
            return -amt
    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds
        else:
            return -amt
    def __str__(self):
        return 'Fair Roulette'
        
    
def playRoulette(game, numSpins, toPrint = True):
    luckyNumber = '2'
    bet = 1
    totRed, totBlack, totPocket = 0.0, 0.0, 0.0
    for _ in range(numSpins):
        game.spin()
        totRed += game.betRed(bet)
        totBlack += game.betBlack(bet)
        totPocket += game.betPocket(luckyNumber, bet)
    if toPrint:
        print(numSpins, 'spins of', game)
        print('Expected return betting red =', str(100*totRed/numSpins) + '%')
        print('Expected return betting black =', str(100*totBlack/numSpins) +
              '%')
        print('Expected return betting', luckyNumber, '=',
              str(100*totPocket/numSpins) + '%\n')
    return (totRed/numSpins, totBlack/numSpins, totPocket/numSpins)

class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        #super.__init__()
        self.pockets.append('0')
    def __str__(self):
        return 'European Roulette'

class AmRoulette(FairRoulette):
    def __init__(self):
        super().__init__()
        self.pockets.append('0')
        self.pockets.append('00')
    def __str__(self):
        return 'AmericanRoulette'

def findPocketReturn(game, numTrials, trialSize, toPrint):
    pocketReturns = list()
    for t in range(numTrials):
        trialVals = playRoulette(game, trialSize, toPrint)
        pocketReturns.append(trialVals[2])
    return pocketReturns

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    X2 = [i*i for i in X]
    mean2 = sum(X2)/float(len(X2))
    std = (mean2 - mean*mean)**0.5
    return mean, std

def main():
    random.seed(0)
    numTrials = 20
    resultDict = {}
    games = (FairRoulette, EuRoulette, AmRoulette)
    for G in games:
        resultDict[G().__str__()] = []
    for numSpins in (100, 1000, 10000):
        print('\nSimulate betting a pocket for', numTrials, 'trials of',
              numSpins, 'spins each')
        for G in games:
            pr = findPocketReturn(G(), numTrials, numSpins, False)
            mean, std = getMeanAndStd(pr)
            resultDict[G().__str__()].append((numSpins, 100*mean, 100*std))
            print('Exp. return for', G(), '=', str(round(100*mean, 3)),
                  '% +-', str(round(196*std,3)), '% with 95% conf')
    numTrials = 50000
    numSpins = 200
    game = FairRoulette()

    means = []
    for i in range(numTrials):
        means.append(findPocketReturn(game, 1, numSpins, False)[0]/numSpins)
    plt.hist(means, bins=19, weights=np.array(len(means)*[1])/len(means))
    plt.xlabel('mean return')
    plt.ylabel('probability')
    plt.title('expected return')
    plt.show()
    

if __name__ == '__main__':
    main()
