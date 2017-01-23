# Link to this kata
# https://www.codewars.com/kata/nesting-structure-comparison

def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for a1, a2 in zip(original, other):
            if not same_structure_as(a1, a2):
                return False
        else:
            return True
    else:
        return not isinstance(original, list) and not isinstance(other, list)