# https://www.codewars.com/kata/after-midnight

def day_and_time(mins):
    day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return '{} {:02d}:{:02d}'.format(day[(mins // 1440) % 7], (mins // 60) % 24, mins % 60)