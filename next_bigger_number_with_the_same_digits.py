# https://www.codewars.com/kata/next-bigger-number-with-the-same-digits

from collections import Counter


def next_bigger(n):
    digits = str(n)
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] > digits[i-1]:
            break
    else:
        return -1

    seen = Counter(digits[i-1:])
    res = digits[:i-1]
    d = digits[i-1]
    for k in '123456789':
        if k > d and k in seen:
            res += k
            seen[k] -= 1
            break

    return int(res + ''.join(k * seen[k] for k in sorted(seen)))