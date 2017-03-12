# https://www.codewars.com/kata/number-of-people-in-the-bus

def number(bus_stops):
    return sum(stop[0] - stop[1] for stop in bus_stops)