# https://www.codewars.com/kata/not-all-but-sometimes-all

def remove(text, what):
    counts = what.copy()
    res = ''
    for c in text:
        if c in counts and counts[c] > 0:
            counts[c] -= 1
        else:
            res += c
    return res