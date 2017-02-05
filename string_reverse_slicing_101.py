# https://www.codewars.com/kata/string-reverse-slicing-101

def reverse_slice(s):
    return [s[i::-1] for i in range(len(s) - 1, -1, -1)]