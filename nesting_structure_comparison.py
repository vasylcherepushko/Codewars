# https://www.codewars.com/kata/nesting-structure-comparison

def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for match in map(same_structure_as, original, other):
            if not match:
                return False
        else:
            return True
    else:
        return not isinstance(original, list) and not isinstance(other, list)