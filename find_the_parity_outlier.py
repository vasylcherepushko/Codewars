# https://www.codewars.com/kata/find-the-parity-outlier

def find_outlier(integers):
    even, odd = 0, 0
    for n in integers[:3]:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    outlier = 1 if even > odd else 0

    for n in integers:
        if n % 2 == outlier:
            return n