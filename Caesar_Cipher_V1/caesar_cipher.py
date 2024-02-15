# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

import string

def shift_character(char, shift, alphabet):
    if char in alphabet:
        index = (alphabet.index(char) + shift) % len(alphabet)
        return alphabet[index]
    else:
        return char

def encode_decode_text(text, shift, alphabet):
    return ''.join(shift_character(char, shift, alphabet) for char in text)

def main():
    alphabet = string.ascii_lowercase
    direction = input('Type "encode" to encrypt or type "decode" to decrypt: ').lower()

    if direction not in ['encode', 'decode']:
        print("Invalid direction. Please enter 'encode' or 'decode'.")
        return

    input_text = input('Type your message: ').lower()
    
    while True:
        shift_input = input('Type the shift number: ')
        try:
            shift = int(shift_input)
            break  # Salir del bucle si la entrada es un número válido
        except ValueError:
            print("Invalid shift value. Please enter a valid integer.")
    
    if direction == 'encode':
        output_text = encode_decode_text(input_text, shift, alphabet)
    elif direction == 'decode':
        output_text = encode_decode_text(input_text, -shift, alphabet)

    print(output_text)

if __name__ == "__main__":
    while True:
        main()