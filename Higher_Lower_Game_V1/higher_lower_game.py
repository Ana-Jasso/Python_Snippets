# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

# Credits for ASCII Art
# Text1: https://patorjk.com/software/taag/#p=display&f=Crawford2&t=Higher-Lower%0A%20%20%20%20%20%20Game
# Text2: https://patorjk.com/software/taag/#p=display&f=Crawford2&t=VS

import os
import random
from ASCII_drawings import game_name, vs
from game_data import data

# print(game_name)
# print(data[0])
# print(vs)

def limpiar_pantalla():
    # Comando para limpiar la pantalla en sistemas basados en Unix (Linux y macOS)
    if os.name == 'posix':
        os.system('clear')
    # Comando para limpiar la pantalla en sistemas basados en Windows
    elif os.name == 'nt':
        os.system('cls')

def obtener_dos_elementos_diferentes(lista):
    elemento_1 = random.choice(lista)
    elemento_2 = random.choice(lista)
    
    while elemento_2 == elemento_1:
        elemento_2 = random.choice(lista)
    
    return elemento_1, elemento_2

continuar = True

while continuar:
    limpiar_pantalla()
    print(game_name)
    A, B = obtener_dos_elementos_diferentes(data)
    print(A)
    print(B)
    #print(f'Compare A: {data['name']}')
    print(vs)
    continuar = False