# https://www.codewars.com/kata/filter-unused-digits

def unused_digits(*args):
    digits = set('0123456789')
    used = set(''.join(str(n) for n in args))
    return ''.join(sorted(digits.difference(used)))