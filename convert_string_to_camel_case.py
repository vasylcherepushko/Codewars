# Link to this kata
# https://www.codewars.com/kata/convert-string-to-camel-case

def to_camel_case(s):
    return s[0] + s.title().translate({ord('-'):None, ord('_'):None})[1:] if s else ''
