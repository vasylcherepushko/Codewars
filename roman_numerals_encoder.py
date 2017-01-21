# Link to this kata
# https://www.codewars.com/kata/51b62bf6a9c58071c600001b

def solution(n):
    NUMERALS = [['M', 'MM', 'MMM'],   
                ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
                ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
                ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']]
    
    res = ''        
    for i, d in enumerate(str(n).zfill(4)):
        res += NUMERALS[i][int(d)-1] if int(d) != 0 else ''
    
    return res   
