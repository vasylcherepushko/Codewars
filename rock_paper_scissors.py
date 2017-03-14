# https://www.codewars.com/kata/rock-paper-scissors

def rps(p1, p2):
    beats = {'scissors':'paper', 'paper':'rock', 'rock':'scissors'}
    if beats[p1] == p2:
        return 'Player 1 won!'
    if beats[p2] == p1:
        return 'Player 2 won!'
    return 'Draw!'