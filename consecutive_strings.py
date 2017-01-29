# Link to this kata
# https://www.codewars.com/kata/consecutive-strings

def longest_consec(a, k):
    if not a or not 0 <= k <= len(a):
        return ''
    return max((''.join(a[i:i+k]) for i in range(len(a) + 1 - k)), key=len)