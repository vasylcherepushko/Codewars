# https://www.codewars.com/kata/count-inversions

def count_inversion(seq):
    res = 0
    for i in range(len(seq) - 1):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                res += 1
    return res