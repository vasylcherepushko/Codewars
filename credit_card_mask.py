# https://www.codewars.com/kata/credit-card-mask

def maskify(cc):
    return cc[-4:].rjust(len(cc), '#')