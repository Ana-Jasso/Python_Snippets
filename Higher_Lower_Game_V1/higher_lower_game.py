# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

# Credits for ASCII Art
# Text1: https://patorjk.com/software/taag/#p=display&f=Crawford2&t=Higher-Lower%0A%20%20%20%20%20%20Game
# Text2: https://patorjk.com/software/taag/#p=display&f=Crawford2&t=VS

import os
import random
from ASCII_drawings import game_name, vs
from game_data import data

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_dos_elementos_diferentes(lista):
    elementos = random.sample(lista, 2)
    return elementos[0], elementos[1]

def solicitar_respuesta():
    # Solicitar respuesta, siempre será tomada en mayúsculas
    answer = input('Who has more followers? Type "A" or "B": ').upper()
    while answer not in ['A', 'B']:
        print("Please enter a valid response (A/B).")
        answer = input('Who has more followers? Type "A" or "B": ').upper()
    return answer

def new_comparison():
    A, B = obtener_dos_elementos_diferentes(data)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    
    if A['follower_count'] >= B['follower_count']:
        respuesta_correcta = 'A'
    else:
        respuesta_correcta = 'B'
    
    # Verificar si el user ganó para devolver el resultado.
    respuesta = solicitar_respuesta()
    if respuesta == respuesta_correcta:
        return True
    else:
        return False

continuar = True
current_score = 0
current_score_text = ''

while continuar:
    limpiar_pantalla()
    print(game_name)
    print(current_score_text)

    resultado = new_comparison()
    
    if resultado:
        current_score += 1
        current_score_text = f"You're right! Current Score: {current_score}"
        continuar = True
    else:
        continuar = False

limpiar_pantalla()
print(game_name)
print(f"Sorry, that's wrong. Final score: {current_score}")