# Link to this kata
# https://www.codewars.com/kata/the-observed-pin

from itertools import product


def get_pins(observed):
    ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')
    return [''.join(p) for p in product(*[ADJACENTS[int(d)] for d in observed])]