# https://www.codewars.com/kata/where-my-anagrams-at

def anagrams(word, words):
    match = sorted(word)
    return [w for w in words if match == sorted(w)]