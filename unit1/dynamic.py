import time

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fastFib(n, memo={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1,memo) + fastFib(n-2,memo)
        memo[n] = result
        return result
    

for i in range(50,150,5):
    s = time.time()
    print(fastFib(i,{}))
    e = time.time()
    print('%.4f'%(e-s))
    print()
