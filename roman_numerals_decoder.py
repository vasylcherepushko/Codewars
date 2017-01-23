# Link to this kata
# https://www.codewars.com/kata/roman-numerals-decoder

def solution(roman):
    VALS = {'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1}
    res = 0
    while roman:
        try:
            if VALS[roman[0]] < VALS[roman[1]]:
                res += VALS[roman[1]] - VALS[roman[0]]
                roman = roman[2:]
            else:
                res += VALS[roman[0]]
                roman = roman[1:]
        except:
            res += VALS[roman[0]]
            break
    return res
    
            