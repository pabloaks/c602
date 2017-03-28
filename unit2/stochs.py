#!/usr/bin/env python3

import matplotlib.pyplot as plt
import random
import numpy as np

def rollDie():
    return random.choice([1,2,3,4,5,6])

def testRoll(n=10):
    result = ''
    for i in range(n):
        result += str(rollDie())
    print(result)

def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print('Actual prob = ',round(1/(6**len(goal)), 8))
    estProbability = round(total/numTrials, 8)
    print('Estimated prob =', round(estProbability, 8))

def fracBoxCars(numTests):
    numBoxCars = 0
    for i in range(numTests):
        if rollDie() == 6 and rollDie() == 6:
            numBoxCars += 1
    return numBoxCars

def roll4die():
    return random.choice([1,2,3,4,5,6,7,8,9,10])



