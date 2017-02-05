# https://www.codewars.com/kata/jaden-casing-strings

def toJadenCase(string):
    return ' '.join(word.capitalize() for word in string.split(' '))