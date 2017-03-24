# https://www.codewars.com/kata/bouncy-numbers

def is_bouncy(number):
    string = str(number)
    increasing, decreasing = True, True
    for d1, d2 in zip(string[:-1], string[1:]):
        if d1 < d2:
            decreasing = False
        if d1 > d2:
            increasing = False
    return not increasing and not decreasing