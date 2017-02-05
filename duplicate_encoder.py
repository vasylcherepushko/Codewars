# https://www.codewars.com/kata/duplicate-encoder

from collections import Counter


def duplicate_encode(word):
    word = word.lower()
    counter = Counter(word)
    return ''.join('(' if counter[c] == 1 else ')' for c in word)