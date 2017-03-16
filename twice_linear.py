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