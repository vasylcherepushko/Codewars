# https://www.codewars.com/kata/pascals-triangle-number-2

def pascal_zip(p):
    triangle = [[1]]
    for _ in range(p - 1):
        to_sum = zip([0] + triangle[-1], triangle[-1] + [0])
        triangle.append(map(sum, to_sum))
    return triangle

def pascal(p):
    res = [[1]]
    while len(res) < p:
        last = res[-1]
        new = [1 if i == 0 or i == len(last) else last[i] + last[i-1] for i in range(len(last)+1)]
        res.append(new)
    return res