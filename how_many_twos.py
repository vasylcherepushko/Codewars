# https://www.codewars.com/kata/how-many-twos

def two_count(n):
  return bin(n)[::-1].index('1')