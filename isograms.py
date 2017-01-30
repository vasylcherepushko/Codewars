# Link to this kata
# https://www.codewars.com/kata/isograms

def is_isogram(string):
    return len(string) == len(set(list(string.lower())))