# Link to this kata
# https://www.codewars.com/kata/roman-numerals-decoder

def solution(roman):
    VALS = {'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1
    }
    total, last = 0, 0
    for d in roman[::-1]:
        if VALS[d] >= last:
            total += VALS[d]
        else:
            total -= VALS[d]
        last = VALS[d]
    return total