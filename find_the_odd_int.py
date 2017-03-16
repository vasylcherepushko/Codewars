# https://www.codewars.com/kata/find-the-odd-int

from collections import Counter


def find_it(seq):
    counter = Counter(seq)
    for i in counter:
        if counter[i] % 2 != 0:
            return i