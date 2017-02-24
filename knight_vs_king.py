# https://www.codewars.com/kata/knight-vs-king

def knightVsKing (knightPosition, kingPosition):
    row = abs(knightPosition[0] - kingPosition[0])
    col = abs(ord(knightPosition[1]) - ord(kingPosition[1]))
    
    if row <= 1 and col <= 1:
        return 'King'
    if (row, col) in ((1, 2), (2, 1)):
        return 'Knight'
    
    return 'None'