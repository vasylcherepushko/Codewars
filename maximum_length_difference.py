# https://www.codewars.com/kata/maximum-length-difference

def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    
    a1_min = a1_max = len(a1[0])
    a2_min = a2_max = len(a2[0])
    
    for s in a1:
        if len(s) < a1_min:
            a1_min = len(s)
        if len(s) > a1_max:
            a1_max = len(s)
    
    for s in a2:
        if len(s) < a2_min:
            a2_min = len(s)
        if len(s) > a2_max:
            a2_max = len(s)
    
    return max(abs(a1_min - a2_max), abs(a1_max - a2_min))