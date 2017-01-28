# Link to this kata
# https://www.codewars.com/kata/decode-the-morse-code

def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))