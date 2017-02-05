# https://www.codewars.com/kata/reverse-or-rotate

def revrot_dense(strng, sz):
    if sz <= 0 or sz > len(strng) or strng == "":
        return ""

    chunks = [strng[i:i+sz] for i in range(0, len(strng) // sz * sz, sz)]

    return "".join(chunk[::-1] if (sum(int(n)**3 for n in chunk) % 2 == 0) else (chunk[1:] + chunk[0]) for chunk in chunks)

def revrot(s, n, res=""):
    if not s or n < 1 or n > len(s):
        return ""

    while len(s) >= n:
        group = s[:n]
        if sum([int(d)**3 for d in group]) % 2 == 0:
            res += group[::-1]
        else:
            res += group[1:] + group[0]
        s = s[n:]

    return res