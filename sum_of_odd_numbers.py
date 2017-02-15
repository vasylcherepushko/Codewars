# https://www.codewars.com/kata/sum-of-odd-numbers 

def row_sum_odd_numbers(n):
    first = ((n - 1) * n / 2 + 1) * 2 - 1
    return sum(first + i * 2  for i in range(n))
    
def def row_sum_odd_numbers_optimal(n):
    return n ** 3