# Link to this kata
# https://www.codewars.com/kata/tribonacci-sequence

def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res