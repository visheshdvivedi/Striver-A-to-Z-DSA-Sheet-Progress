def fib(n, cache):
    if n in cache:
        return cache[n]
    cache[n] = fib(n-1, cache)+fib(n-2, cache)
    return cache[n]

cache = {0: 0, 1: 1, 2: 1}
num = int(input())
print(fib(num, cache))