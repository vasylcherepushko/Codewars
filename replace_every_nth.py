# https://www.codewars.com/kata/replace-every-nth

def replace_nth(text, n, old, new):
    res = ''
    skip = n - 1
    for char in text:
        if char == old and skip:
            res += char
            skip -= 1
        elif char == old and not skip:
            res += new
            skip = n - 1
        else:
            res += char
    return res