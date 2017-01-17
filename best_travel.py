from itertools import combinations


def choose_best_sum(t, k, ls):
    res = 0
    for c in combinations(ls, k):
        if res < sum(c) <= t:
            res = sum(c)
    if res == 0:
        return None
    return res
