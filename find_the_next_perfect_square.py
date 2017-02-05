# https://www.codewars.com/kata/find-the-next-perfect-square

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1) ** 2
    return -1