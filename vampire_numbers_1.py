# https://www.codewars.com/kata/vampire-numbers-1

from collections import Counter


def vampire_test(x, y):
    return Counter(str(x * y)) == Counter(str(x) + str(y))