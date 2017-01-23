# Link to this kata
# https://www.codewars.com/kata/hamming-numbers
# Inspired by https://www.codewars.com/kata/reviews/5672692ee3659e3f8a00000c/groups/5672692ee3659e3f8a000010

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

def hamming_alternative(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]

	for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)

	return hamms[-1]