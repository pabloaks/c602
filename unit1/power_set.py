##Juan Pablo Robles
### using binary strings
def powerSet(items):
    N = len(items)
    for i in range(2**N):
        yield [items[i] for i, j in enumerate(bin(i)[2:].zfill(N)) if j == '1']

### using itertools
def powerSetB(items):
    import itertools
    N = len(items)
    for i in range(N+1):
        for j in itertools.combinations(items,i):
            yield list(j)
           
def main():
    sampleList = ['car', 'shoe', 'phone']
    for i in powerSet(sampleList):
        print(i)
    print('\n')
    for i in powerSetB(sampleList):
        print(i)

if __name__ == '__main__':
    main()
