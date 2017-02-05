# https://www.codewars.com/kata/tortoise-racing

def race(v1, v2, g):
    if v1 >= v2:
        return
    seconds = int(g * 3600 / (v2 - v1))
    return [seconds // 3600, seconds % 3600 // 60, seconds % 60]