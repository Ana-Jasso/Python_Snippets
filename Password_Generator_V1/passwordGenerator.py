# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = '!#$%&()*+'

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = [random.choice(letters) for _ in range(nr_letters)]
password += [random.choice(symbols) for _ in range(nr_symbols)]
password += [random.choice(numbers) for _ in range(nr_numbers)]

random.shuffle(password)
password = ''.join(password)

print(f'Contraseña: {password}')