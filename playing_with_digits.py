# Link to this kata
# https://www.codewars.com/kata/playing-with-digits

def dig_pow(n, p):
    k = sum(int(d)**(p+i) for i, d in enumerate(str(n))) / n
    if k.is_integer():
        return k
    return -1