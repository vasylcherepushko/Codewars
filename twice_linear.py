# https://www.codewars.com/kata/twice-linear

from collections import deque


def dbl_linear(n):
    x = 1
    q2, q3 = deque([]), deque([])
    for _ in range(n):
        q2.append(2 * x + 1)
        q3.append(3 * x + 1)
        x = min(q2[0], q3[0])
        if x == q2[0]: x = q2.popleft()
        if x == q3[0]: x = q3.popleft()
    return x

def dbl_linear_bruteforce(n):
    seq = {1}
    i = 1
    while len(seq) - 1 < n:
        i += 1
        q2, r2 = divmod(i - 1, 2)
        q3, r3 = divmod(i - 1, 3)
        if (r2 == 0 and q2 in seq) or (r3 == 0 and q3 in seq):
            seq.add(i)
    return i