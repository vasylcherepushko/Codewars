# Link to this kata
# https://www.codewars.com/kata/get-the-middle-character

def get_middle(s):
    mid, odd = divmod(len(s), 2)
    return s[mid] if odd else s[mid-1:mid+1]