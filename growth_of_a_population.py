# Link to this kata
# https://www.codewars.com/kata/growth-of-a-population/

def nb_year(p0, percent, aug, p):
    current = p0
    i = 0
    while current < p:
        current += current * percent / 100 + aug
        i += 1
    return i