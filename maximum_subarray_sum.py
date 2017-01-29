# Link to this kata
# https://www.codewars.com/kata/maximum-subarray-sum

def maxSequence(arr):
    n = len(arr)
    if n <= 1:
        return sum(arr)
    mid = n // 2
    L = maxSequence(arr[:mid])
    R = maxSequence(arr[mid:])
    M = max(sum(arr[i:mid]) for i in range(mid-1, -1, -1)) \
        + max(sum(arr[mid:i]) for i in range(mid+1, n+1))
    return max(L, R, M)

def kadane(arr):
    lowest = res = total = 0
    for n in arr:
        total += n
        lowest = min(lowest, total)
        res = max(res, total - lowest)
    return res