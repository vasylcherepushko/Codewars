# Link to this kata
# https://www.codewars.com/kata/alternating-loops

def combine(*args):
    res = []
    dimensions = [len(x) for x in args]
    total = sum(dimensions)
    while len(res) < total:
        for i, n in enumerate(dimensions):
            if n:
                res.append(args[i][-n])
                dimensions[i] -= 1
    return res