# https://www.codewars.com/kata/hamming-numbers

from collections import deque


def hamming(n):
    seq = [1]
    q2, q3, q5 = deque([2]), deque([3]), deque([5])

    while len(seq) < n:
        x = min(q2[0], q3[0], q5[0])
        if x == q2[0]: x = q2.popleft()
        if x == q3[0]: x = q3.popleft()
        if x == q5[0]: x = q5.popleft()
        seq.append(x)
        q2.append(2 * x)
        q3.append(3 * x)
        q5.append(5 * x)

    return seq[-1]