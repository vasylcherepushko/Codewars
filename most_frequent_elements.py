# http://www.codewars.com/kata/most-frequent-elements

from collections import Counter


def find_most_frequent(arr):
    count = Counter(arr)
    m = max(count.values()) if arr else None
    return set(i for i in count if count[i] == m)