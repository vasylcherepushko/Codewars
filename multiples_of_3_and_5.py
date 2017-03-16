# https://www.codewars.com/kata/multiples-of-3-and-5

def solution(number):
    multiples_3 = sum(range(3, number, 3))
    multiples_5 = sum(range(5, number, 5))
    multiples_15 = sum(range(15, number, 15))
    return multiples_3 + multiples_5 - multiples_15