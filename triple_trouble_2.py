# https://www.codewars.com/kata/triple-trouble-2

def triple_trouble(one, two, three):
    res = ''
    for a, b, c in zip(one, two, three):
        res += a + b + c
    return res