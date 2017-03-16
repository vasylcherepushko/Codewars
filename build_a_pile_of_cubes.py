# https://www.codewars.com/kata/build-a-pile-of-cubes

def find_nb(m):
    n = int((4 * m) ** 0.25)
    cubes = int((n * (n + 1) / 2)) ** 2
    if cubes == m:
        return n
    return -1