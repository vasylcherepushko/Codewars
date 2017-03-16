# https://www.codewars.com/kata/do-i-get-a-bonus

def bonus_time(salary, bonus):
    return '${0}'.format(salary * (10 if bonus else 1))