# Link to this kata
# https://www.codewars.com/kata/roman-numerals-encoder

def solution(n, res=''):
    NUMERALS = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    for k in sorted(NUMERALS.keys(), reverse=True):
        while n >= k:
            res += NUMERALS[k]
            n -= k
    return res