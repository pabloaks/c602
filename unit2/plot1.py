#!/usr/bin/env python3

import pylab as plt
import random
import numpy as np

mySamples =  list()
myLinear = list()
myQuadratic = list()
myCubic = list()
myExponential  = list()

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

plt.figure('lin quad')
plt.plot(mySamples, myLinear, label = 'linear')
plt.plot(mySamples, myQuadratic, label = 'quad')
plt.legend(loc='upper left')

plt.figure('cubic expo')
plt.plot(mySamples, myCubic, label = 'cubic')     
plt.plot(mySamples, myExponential, label = 'expo')
plt.yscale('log')
plt.legend()
plt.show()

