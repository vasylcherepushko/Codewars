# https://www.codewars.com/kata/how-many-stairs-will-suzuki-climb-in-20-years

def stairs_in_20(stairs):
    return sum(sum(weekday) for weekday in stairs) * 20