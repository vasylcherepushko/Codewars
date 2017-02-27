# https://www.codewars.com/kata/knight-vs-king

def knightVsKing (knightPosition, kingPosition):
    dx = abs(knightPosition[0] - kingPosition[0])
    dy = abs(ord(knightPosition[1]) - ord(kingPosition[1]))

    if dx <= 1 and dy <= 1:
        return 'King'
    if (dx, dy) in ((1, 2), (2, 1)):
        return 'Knight'

    return 'None'