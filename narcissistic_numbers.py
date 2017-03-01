# https://www.codewars.com/kata/narcissistic-numbers

def is_narcissistic(n):
    s = str(n)
    return sum(int(d) ** len(s) for d in s) == n