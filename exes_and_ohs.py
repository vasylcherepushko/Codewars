# https://www.codewars.com/kata/exes-and-ohs

def xo(s):
    diff = 0
    for char in s.lower():
        if char == 'x':
            diff += 1
        elif char == 'o':
            diff -= 1
    return not diff