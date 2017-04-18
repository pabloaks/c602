#!/usr/bin/env python3

import random
import numpy as np
import matplotlib.pyplot as plt

def makeHist(data, title, xlabel,ylabel, bins=20):
    plt.hist(data, bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

def getHighs():
    f = open('temperatures.csv')
    pop = []
    for l in f:
        try:
            tempC = float(l.split(',')[1])
            pop.append(tempC)
        except:
            continue
    return pop

def getMeansAndSDs(population, sample, verbose=False):
    popMean = sum(population)/len(population)
    sampleMean = sum(sample)/len(sample)
    if verbose:
        makeHist(population, 'DH pop\nmean = '+str(round(popMean,2)),
                 'degrees', 'number days')
        plt.figure()
        makeHist(sample, 'DH sample\nmean = '+str(round(sampleMean,2)),
                 'degrees', 'number days')
        print('pop mean = ',str(round(popMean, 3)))
        print('sd pop = ', round(np.std(population),4))
        print('samp mean = ', round(sampleMean, 3))
        print('sd samp = ', round(np.std(sample),4))
    return popMean, sampleMean, np.std(population), np.std(sample)

def showErrorBars(population, sizes, numTrials):
    xVals = []
    sizeMeans, sizeSDs = [], []
    for sampleSize in sizes:
        xVals.append(sampleSize)
        trialMeans = []
        for _ in range(numTrials):
            sample = random.sample(population, sampleSize)
            popMean, sampleMean, popSD, sampleSD =\
                     getMeansAndSDs(population, sample, False)
            trialMeans.append(sampleMean)
        sizeMeans.append(np.mean(trialMeans))
        sizeSDs.append(np.std(trialMeans))
    plt.errorbar(xVals, sizeMeans, yerr=1.96*np.array(sizeSDs), fmt='o',
                   label = '95%CI')
    plt.title('Mean Temperature (' + str(numTrials) + ' trials)')
    plt.xlabel('Sample Size')
    plt.ylabel('Mean')
    plt.axhline(y = popMean, color ='r', label = 'Population Mean')
    plt.xlim(0, sizes[-1] + 10)
    plt.legend()
    

def main():
    random.seed(0)
    population = getHighs()
    sampleSize = 800
    numSamples = 500
    maxMeanDiff = 0
    maxSDDiff = 0
    sampleMeans = []
    for _ in range(numSamples):
        sample = random.sample(population, sampleSize)
        pM, sM, pSD, sSD = getMeansAndSDs(population, sample, False)
        sampleMeans.append(sM)
        if abs(pM - sM) > maxMeanDiff:
            maxMeanDiff = abs(pM - sM)
        if abs(pSD - sSD) > maxSDDiff:
            maxSDDiff = abs(pSD - sSD)
    print('mean of sample means: ', round(sum(sampleMeans)/len(sampleMeans),3))
    print('sd of sample means: ', round(np.std(sampleMeans), 3))
    print('max difference in means: ', round(maxMeanDiff, 3))
    print('max diff in sd: ', round(maxSDDiff, 3))
    makeHist(sampleMeans, 'means of samples', 'mean', 'frequency')
    plt.axvline(x=pM, color='r')
    plt.show()

def plotDists():
    uniform, normal, exp = [], [], []
    for _ in range(100000):
        uniform.append(random.random())
        normal.append(random.gauss(0,1))
        exp.append(random.expovariate(0.5))
    makeHist(uniform, 'uniform', 'value', 'frequency', bins=30)
    plt.figure()
    makeHist(normal, 'gaussian', 'value', 'frequency', bins=30)
    plt.figure()
    makeHist(exp, 'exp', 'value', 'frequency', bins=30)
    plt.show()

if __name__ == '__main__':
    sampleSizes = (25, 50, 100, 200, 300, 400, 500, 600)
    numTrials = 100
    population = getHighs()
    popSD = np.std(population)
    sems = []
    sampleSDs = []
    for size in sampleSizes:
        sems.append(popSD/np.sqrt(size))
        means = []
        for t in range(numTrials):
            sample = random.sample(population, size)
            means.append(np.mean(sample))
        sampleSDs.append(np.std(means))
    plt.plot(sampleSizes, sampleSDs, label='std of 50 means')
    plt.plot(sampleSizes, sems, 'r--', label='SEM')
    plt.legend()
    plt.show()
    plotDists()
        
    
