# https://www.codewars.com/kata/maximum-subarray-sum

def maxSequence_recursive(arr):
    n = len(arr)
    if n <= 1:
        return sum(arr)
    mid = n // 2
    L = maxSequence(arr[:mid])
    R = maxSequence(arr[mid:])
    M = max(sum(arr[i:mid]) for i in range(mid-1, -1, -1)) \
        + max(sum(arr[mid:i]) for i in range(mid+1, n+1))
    return max(L, R, M)

def maxSequence(arr):
    lowest = ans = total = 0
    for i in arr:
        total += i
        lowest = min(lowest, total)
        ans = max(ans, total - lowest)
    return ans