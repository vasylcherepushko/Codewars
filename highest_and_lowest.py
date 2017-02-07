# https://www.codewars.com/kata/highest-and-lowest

def high_and_low(numbers):
    low, high = None, None
    start, end = 0, 0
    n = len(numbers)

    for i in range(n):
        if numbers[i] == ' ' or i == n - 1:
            end = i if i != n - 1 else i + 1
            num = int(numbers[start:end])
            if low is None or num < low:
                low = num
            if high is None or num > high:
                high = num
            start = i + 1

    return '{0} {1}'.format(high, low)