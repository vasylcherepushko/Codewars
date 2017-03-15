# https://www.codewars.com/kata/evil-or-odious

def evil(n):
    return "It's {0}!".format(['Evil', 'Odious'][bin(n).count('1') % 2])