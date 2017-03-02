# https://www.codewars.com/kata/down-arrow-with-numbers

def get_a_down_arrow_of(n):
    digits = '1234567890'
    res = ''
    for i in range(n, 0, -1):
        repeat, rest = divmod((2 * i - 1) // 2, 10)
        mid = digits[rest]
        start = digits * repeat + digits[:rest]
        end = start[::-1]
        res += ' ' * (n - i) + start + mid + end + '\n'
    return res.rstrip()