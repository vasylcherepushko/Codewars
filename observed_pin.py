# Link to this kata
# https://www.codewars.com/kata/the-observed-pin

def get_pins(observed):
    adjacent = {
                '1': ['1', '2', '4'],
                '2': ['2', '1', '3', '5'],
                '3': ['3', '2', '6'],
                '4': ['4', '1', '5', '7'],
                '5': ['5', '2', '4', '6', '8'],
                '6': ['6', '3', '5', '9'],
                '7': ['7', '4', '8'],
                '8': ['8', '5', '7', '9', '0'],
                '9': ['9', '6', '8'],
                '0': ['0', '8']
               }
    pool = []
    for i in observed:
        pool.append(adjacent[i])
    
    def func(x, y):
        res = []
        for i in x:
            for j in y:
                res.append(i+j)
        return res
    
    while len(pool) > 1:
        new = func(pool[-2], pool[-1])
        pool.pop()
        pool.pop()
        pool.append(new)
    
    return pool[0]
