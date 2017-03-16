# https://www.codewars.com/kata/maximum-subarray-sum

def maxSequence(arr):
    lowest = res = total = 0
    for n in arr:
        total += n
        lowest = min(lowest, total)
        res = max(res, total - lowest)
    return res