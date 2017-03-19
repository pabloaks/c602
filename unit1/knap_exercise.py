#!/usr/bin/env python3

class Item(object):

    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        a = 'item: %s - weighs %.2f for a value of %.2f' \
            %(self.name, self.weight, self.value)
        return a

class Knapsack(object):

    def __init__(self, list_candidates, weight):
        self.list_cand = list_candidates
        self.included = list()
        self.weight_limit = weight

    def runHeuristic(self, met):
        self.included = list()
        priority = sorted(self.list_cand, key=met, reverse=True)
        curr_weight = 0.00
        for i in priority:
            if i.getWeight() <= self.weight_limit - curr_weight \
               and i.getValue() > 0:
                    self.included.append(i)
                    curr_weight += i.getWeight()
        print('ITEMS in the KS: ')
        [print(i) for i in self.included]
        print('TW: %.2f of possible %.2f'%(curr_weight, self.weight_limit))
        return self.included

def metric1(item):
    try:
        return item.getValue()/item.getWeight()
    except:
        if item.getValue() > 0:
            return 9e100
        else:
            return -9e100

def metric2(item):
    return item.getWeight()

def metric3(item):
    return item.getValue()

def main():
    candidates = list()
    food = ['wine', 'beer', 'pizza', 'burger', 'fries', 'coke', 'apple', 'donut']
    value = [89,90,95,100,90,79,50,10]
    calories = [123,154,258,354,365,150,95,195]
    for i,j,k in zip(food, value, calories):
        candidates.append(Item(i,j,k))


    ks = Knapsack(candidates, 1000)
    print('\n\nMetric: RATIO')
    ks.runHeuristic(metric1)
    print('\n\nMetric: WEIGHT')
    ks.runHeuristic(lambda x: 1/metric2(x))
    print('\n\nMetric: VALUE')
    ks.runHeuristic(metric3)
    
if __name__ == '__main__':
    main()
    
