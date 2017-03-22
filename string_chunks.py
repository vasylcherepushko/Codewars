# https://www.codewars.com/kata/string-chunks

def string_chunk(string, n=0):
    if not isinstance(n, int) or n <= 0:
        return []
    return [string[i:i+n] for i in range(0, len(string), n)]