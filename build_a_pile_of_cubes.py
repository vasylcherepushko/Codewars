# https://www.codewars.com/kata/build-a-pile-of-cubes

def find_nb_bruteforce(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1

def find_nb(m):
    n = int((4 * m) ** 0.25)
    cubes = int((n * (n + 1) / 2)) ** 2
    if cubes == m:
        return n
    return -1