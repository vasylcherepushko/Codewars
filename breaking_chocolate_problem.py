# https://www.codewars.com/kata/breaking-chocolate-problem

def breakChocolate(n, m):
    if n <= 0 or m <= 0:
        return 0
    return (n - 1) + n * (m - 1)