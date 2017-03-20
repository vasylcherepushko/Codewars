# https://www.codewars.com/kata/character-frequency-2

def char_freq(message):
    res = {}
    for c in message:
        res[c] = res.get(c, 0) + 1
    return res