# https://www.codewars.com/kata/consecutive-strings

def longest_consec(a, k):
    if not a or not 0 <= k <= len(a):
        return ''
    current = sum(len(a[i]) for i in range(k))
    longest = current
    longest_start = 0
    for i in range(1, len(a) + 1 - k):
        current -= len(a[i-1])
        current += len(a[i-1+k])
        if current > longest:
            longest_start = i
            longest = current
    return ''.join(a[longest_start:longest_start+k])