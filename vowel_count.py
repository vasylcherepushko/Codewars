# https://www.codewars.com/kata/vowel-count

def getCount(inputStr):
    return sum(1 for char in inputStr if char in 'aeiouAEIOU')