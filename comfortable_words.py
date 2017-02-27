# https://www.codewars.com/kata/comfortable-words

def comfortable_word(word):
    left = 'qwertasdfgzxcvb'
    right = 'yuiophjklnm'
    previous_in_left = True if word[0] in left else False

    for letter in word[1:]:
        if letter in left and previous_in_left:
            return False
        if letter in right and not previous_in_left:
            return False
        previous_in_left = not previous_in_left

    return True