# https://www.codewars.com/kata/collatz-conjecture-length

def collatz(n):
    res = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        res += 1
    return res