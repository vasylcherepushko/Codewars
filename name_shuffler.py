# https://www.codewars.com/kata/name-shuffler

def name_shuffler(s):
    first, last = s.split(' ')
    return last + ' ' + first