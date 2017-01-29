# Link to this kata
# https://www.codewars.com/kata/best-travel

from itertools import combinations


def choose_best_sum(t, k, a):
    try:
        return max(sum(c) for c in combinations(a, k) if sum(c) <= t)
    except:
        return None