# https://www.codewars.com/kata/no-zeros-for-heros

def no_boring_zeros(n):
    if n == 0:
        return 0

    while n % 10 == 0:
        n /= 10
    return n