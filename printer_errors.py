# https://www.codewars.com/kata/printer-errors

def printer_error(s):
    errors = 0
    for c in s:
        if c > 'm':
            errors += 1
    return '{0}/{1}'.format(errors, len(s))