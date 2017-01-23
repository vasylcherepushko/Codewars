# Link to this kata
# https://www.codewars.com/kata/growth-of-a-population

def nb_year(population, percent, increment, target):
    years = 0
    while population < target:
        population += population * percent / 100 + increment
        years += 1
    return years