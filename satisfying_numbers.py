# https://www.codewars.com/kata/satisfying-numbers

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def smallest(n):
    res = 1

    for i in range(2, n + 1):
        res *= i / gcd(i, res)

    return res