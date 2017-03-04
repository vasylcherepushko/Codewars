# https://www.codewars.com/kata/cyclops-numbers

def cyclops (n):
    binary = bin(n)[2:]
    mid, odd = divmod(len(binary), 2)
    if odd and binary[mid] == '0' and binary.count('0') == 1:
        return True
    return False