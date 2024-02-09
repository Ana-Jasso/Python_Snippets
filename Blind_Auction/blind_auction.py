# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

# Credits for ASCII Art
# Drawing: https://ascii.co.uk/art/gavel
# Text: https://ascii.co.uk/art/auction

import os

def display_Ascii_text():
    print("""
                  _   _             
                 | | (_)            
  __ _ _   _  ___| |_ _  ___  _ __  
 / _` | | | |/ __| __| |/ _ \| '_ \ 
| (_| | |_| | (__| |_| | (_) | | | |
 \__,_|\__,_|\___|\__|_|\___/|_| |_|
                                    
    """)

def display_gavel():
    print("""
         ___________
         \         /
          )_______(
          |"""""""|_.-._,.---------.,_.-._
          |       | | |               | | ''-.
          |       |_| |_             _| |_..-'
          |_______| '-' `'---------'` '-' 
          )"""""""(
         /_________\\
         `'-------'`
       .-------------.
   /_______________\\
    """)

def imprimir_bienvenida():
    display_Ascii_text()
    display_gavel()

def limpiar_pantalla():
    # Comando para limpiar la pantalla en sistemas basados en Unix (Linux y macOS)
    if os.name == 'posix':
        os.system('clear')
    # Comando para limpiar la pantalla en sistemas basados en Windows
    elif os.name == 'nt':
        os.system('cls')

def recolectar_informacion(diccionario, clave, oferta):
    diccionario[clave] = int(oferta)
    return diccionario

terminar = False
players_dict = {}

while not terminar:
    limpiar_pantalla()
    imprimir_bienvenida()
    
    key = input('What is your name? ')

    # Validar que 'key' sea un string
    while not key.isalpha():
        print("Please enter a valid name (letters only).")
        key = input('What is your name? ')

    bid = input('What is your bid? $')

    # Validar que 'bid' sea un número
    while not bid.replace('.', '', 1).isdigit():
        print("Please enter a valid bid (numeric value).")
        bid = input('What is your bid? $')

    players_dict = recolectar_informacion(players_dict, key, bid)

    condicion = input('There is another person that wants to bid? (y/n) ')

    # Validar la respuesta de 'condicion'
    while condicion.lower() not in ['yes', 'y', 'no', 'n', 'sure']:
        print("Please enter a valid response (y/n).")
        condicion = input('There is another person that wants to bid? (y/n) ')

    if condicion.lower() in ['no', 'n']:
        highest_bid = max(players_dict.values())
        player_with_highest_bid = max(players_dict, key=players_dict.get)
        terminar = True

limpiar_pantalla()
imprimir_bienvenida()
empates = [jugador for jugador, oferta in players_dict.items() if oferta == highest_bid]

if len(empates) == 1:
    print(f'El jugador con la apuesta más alta es: {empates[0]} con ${highest_bid}.')
else:
    print('Empate entre los siguientes jugadores:')
    for empate in empates:
        print(f'{empate} con ${highest_bid}.')