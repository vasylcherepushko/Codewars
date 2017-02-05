# https://www.codewars.com/kata/multiples-of-3-and-5

def solution_formula(number):
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result

def solution(number):
    multiples_3 = sum(range(3, number, 3))
    multiples_5 = sum(range(5, number, 5))
    multiples_15 = sum(range(15, number, 15))
    return multiples_3 + multiples_5 - multiples_15