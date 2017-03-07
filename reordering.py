# https://www.codewars.com/kata/reordering

def re_ordering(text):
    if text[0].isupper():
        return text
        
    words = text.split(' ')
    for i, word in enumerate(words):
        if word[0].isupper():
            return '{0} {1}'.format(words.pop(i), ' '.join(words))