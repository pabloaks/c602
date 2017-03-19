#!/usr/bin/env python3
from knap_exercise import Item
from knap_exercise import Knapsack as ks

class Node(object):

    def __init__(self, parent, l_in, l_out, l_avail):
        self.parent = parent
        self.nodeLeft = None
        self.nodeRight = None
        self.listIn = l_in
        self.listOut = l_out
        self.listAvail = l_avail
        
# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i//(2**j)) % 2 == 1:
                combo.append(items[j])
        yield combo

def powerSet3(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        combo1 = []
        combo2 = []
        for j in range(N):
            if (i//(3**j)) % 3 == 1:
                combo1.append(items[j])
            elif (i//(3**j)) % 3 == 2:
                combo2.append(items[j])
        yield (combo1, combo2)

def powerSetB(items):
    N = len(items)
    for i in range(2**N):
        combo = list()
        temp = bin(i)[2:].zfill(N)
        for i,j in enumerate(temp):
            if j == '1':
                combo.append(items[i])
        yield combo

def main():
    ll = ['car', 'shoe', 'phone', 'laptop']
    for i in powerSetB(ll):
        print(i)
    print()
    for i in powerSet(ll):
        print(i)


if __name__ == '__main__':
    main()
