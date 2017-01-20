# Link to this kata
# https://www.codewars.com/kata/520446778469526ec0000001

def same_structure_as(original, other):  
    if not (isinstance(original, list) and isinstance(other, list)):
        return False
    if len(original) != len(other):
        return False
    for x, y in zip(original, other):
        first = isinstance(x, list)
        second = isinstance(y, list)
        if first != second:
            return False
        if first and second:
            if same_structure_as(x, y):
                continue
            else:
                return False
    return True
