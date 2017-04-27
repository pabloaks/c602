#!/usr/bin/env python3

import random
import matplotlib.pyplot as plt
import numpy as np

def getData(filename):
    dataFile = open(filename, 'r')
    distances = list()
    masses = list()
    dataFile.readline()
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

def aveMeanSquareError(data, predicted):
    error = 0.0
    for i, j in zip(data, predicted):
        error += (i - j)**2
    return error/len(data)

def rSquared(obs, pred):
    error = ((pred - obs)**2).sum()
    meanError = error/len(obs)
    return 1 - (meanError/np.var(obs))

def fitData(filename):
    xVals, yVals = getData(filename)
    xVals = np.array(xVals)
    yVals = np.array(yVals)
    xVals = xVals*9.81
    plt.plot(xVals, yVals, 'bo', label='Measured points')
    model1 = np.polyfit(xVals, yVals, 1)
    estYVals = np.polyval(model1, xVals)
    model2 = np.polyfit(xVals, yVals, 2)
    estYVals2 = np.polyval(model2, xVals)
    plt.plot(xVals, estYVals, 'r', label='Linear Fit')
    plt.plot(xVals, estYVals2, 'g', label='Quad Fit')
    plt.legend(loc='best')
    plt.show()
    print(aveMeanSquareError(yVals, estYVals))
    print(aveMeanSquareError(yVals, estYVals2))

def genFits(xVals, yVals, degrees):
    models = []
    for d in degrees:
        model = np.polyfit(xVals, yVals, d)
        models.append(model)
    return models

def testFits(models, degrees, xVals, yVals, title):
    plt.plot(xVals, yVals, 'o', label='Data')
    for m, d in zip(models, degrees):
        estYVals = np.polyval(m, xVals)
        error = rSquared(yVals, estYVals)
        plt.plot(xVals, estYVals, label='fit of degree '+str(d)+' r2 = '+
                 str(round(error,4)))
    plt.legend(loc='best')
    plt.title(title)
    plt.show()

def fitData2(filename):
    xVals, yVals = getData(filename)
    xVals = np.array(xVals)
    yVals = np.array(yVals)
    xVals = xVals*9.81
    degrees = [1, 2, 3]
    models = genFits(xVals, yVals, degrees)
    testFits(models, degrees, xVals, yVals, 'title')

def genNoisyData(a, b, c, xVals, fname):
    yVals =[]
    for x in xVals:
        theo = a*x**2 + b*x + c
        yVals.append(random.gauss(theo, 35))
    f = open(fname, 'w')
    f.write('x\t\ty\n')
    for x, y in zip(xVals, yVals):
        f.write(str(y)+'\t'+str(x)+'\n')
    f.close()

class tempDatum(object):
    def __init__(self, s):
        info = s.split(',')
        self.high = float(info[1])
        self.year = int(info[2][0:4])
    def getHigh(self):
        return self.high
    def getYear(self):
        return self.year

def getTempData():
    inF = open('temperatures.csv')
    data = []
    inF.readline()
    for l in inF:
        data.append(tempDatum(l))
    return data
def getYearlyMeans(data):
    years = {}
    for d in data:
        try:
            years[d.getYear()].append(d.getHigh())
        except:
            years[d.getYear()] = [d.getHigh()]
    for y in years:
        years[y] = np.average(years[y])
    return years

def splitData(xVals, yVals):
    toTrain = random.sample(range(len(xVals)), len(xVals)//2)
    trainX, trainY, testX, testY = [], [], [], []
    for i in range(len(xVals)):
        if i in toTrain:
            trainX.append(xVals[i])
            trainY.append(yVals[i])
        else:
            testX.append(xVals[i])
            testY.append(yVals[i])
    return trainX, trainY, testX, testY

def splitData2(xVals, yVals):
    shuff = np.arange(len(xVals))
    random.shuffle(shuff)
    toTrain = shuff[:len(xVals)//2]
    toTest = shuff[len(xVals)//2:]
    x = np.array(xVals)
    y = np.array(yVals)
    trainX = list(x[toTrain])
    trainY = list(y[toTrain])
    testX = list(x[toTest])
    testY = list(y[toTest])
    return trainX, trainY, testX, testY

def main():
    data = getTempData()
    years = getYearlyMeans(data)
    xVals, yVals = [], []
    for e in years:
        xVals.append(e)
        yVals.append(years[e])
    plt.plot(xVals, yVals)
    plt.xlabel('year')
    plt.ylabel('mean daily high')
    plt.title('select US cities')
    plt.show()
    numSubsets = 10
    dimensions = (1, 2, 3)
    rSquares = {}
    for d in dimensions:
        rSquares[d] = []
    
    for f in range(numSubsets):
        trainX, trainY, testX, testY = splitData2(xVals, yVals)
        for d in dimensions:
            model = np.polyfit(trainX, trainY, d)
            estYVals = np.polyval(model, testX)
            rSquares[d].append(rSquared(testY, estYVals))
    print('Mean r-squares for test data')
    for d in dimensions:
        mean = np.average(rSquares[d])
        sd = np.std(rSquares[d])
        print('for dim %d, mean: %.4f sd: %.4f'%(d, mean, sd))


if __name__ == '__main__':
    main()
        
