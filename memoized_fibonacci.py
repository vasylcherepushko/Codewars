# https://www.codewars.com/kata/memoized-fibonacci

def memoize(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]

    return wrapper

@memoize
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)