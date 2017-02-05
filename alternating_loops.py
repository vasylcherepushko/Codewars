# https://www.codewars.com/kata/alternating-loops

def combine(*args):
    res = []
    for i in range(len(max(args, key=len))):
        for arr in args:
            if i < len(arr):
		        res.append(arr[i])
    return res