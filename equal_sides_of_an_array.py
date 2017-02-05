# https://www.codewars.com/kata/equal-sides-of-an-array

def find_even_index(arr):
    left = 0
    right = sum(arr)

    for pos, n in enumerate(arr):
        right -= n
        if left == right:
            return pos
        left += n

    return -1