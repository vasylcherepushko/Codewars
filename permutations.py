# https://www.codewars.com/kata/permutations

def permutations_generator(s):
    n = len(s)
    pool = tuple(s)
    indices = list(range(n))
    yield ''.join(tuple(pool[i] for i in indices))
    while indices != list(range(n-1, -1, -1)):
        for i in range(n-1, -1, -1):
            if indices[i-1] < indices[i]:
                break
        else:
            return
        for j in range(n-1, i-1, -1):
            if indices[i-1] < indices[j]:
                indices[i-1], indices[j] = indices[j], indices[i-1]
                indices[i:] = sorted(indices[i:])
                break

        yield ''.join(tuple(pool[i] for i in indices))

def permutations(string):
    return list(p for p in set(permutations_generator(string)))