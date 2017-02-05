# https://www.codewars.com/kata/counting-duplicates

from collections import Counter


def duplicate_count(text):
    counter = Counter(text.lower())
    res = 0
    for char in counter:
        if counter[char] > 1:
            res += 1
    return res