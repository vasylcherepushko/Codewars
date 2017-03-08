# https://www.codewars.com/kata/split-string-by-multiple-delimiters

def multiple_split(string, delimiters=[]):
    res = []
    start = None
    for i, c in enumerate(string):
        if start is None and c not in delimiters:
            start = i
        if start is not None and c in delimiters:
            res.append(string[start:i])
            start = None
    if start is not None:
        res.append(string[start:])
    return res