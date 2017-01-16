# Link to this kata
# https://www.codewars.com/kata/convert-string-to-camel-case/

def to_camel_case(text):
    if not text:
        return text
    low = text[0].islower()
    res = text.title().replace("-", "").replace("_", "")
    if low:
        return res[0].lower() + res[1:]
    return res
