# Link to this kata
# https://www.codewars.com/kata/tribonacci-sequence

def tribonacci(signature,n):
    res = signature[:n]
    for i in range(n-3):
        res.append(res[-3] + res[-2] + res[-1])
    return res