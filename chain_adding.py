# Link to this kata
# https://www.codewars.com/kata/a-chain-adding-function

class add(int):
    def __call__(self, n):
        return add(self + n)
