# https://www.codewars.com/kata/recursive-reverse-string

def reverse(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse(s[:-1])