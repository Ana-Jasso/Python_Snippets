# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

# Credits for ASCII Art
# Text: https://ascii.co.uk/art/blackjack
# Draw: https://www.asciiart.eu/miscellaneous/playing-cards

import os

def display_Ascii_art():
    ascii_art = """
    _____
    |A .  | _____                    _     _            _    _            _    
    | /.\ ||A ^  | _____            | |   | |          | |  (_)          | |
    |(_._)|| / \ ||A _  | _____     | |__ | | __ _  ___| | ___  __ _  ___| | __
    |  |  || \ / || ( ) ||A_ _ |    | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |____V||  .  ||(_'_)||( v )|    | |_) | | (_| | (__|   <| | (_| | (__|   < 
           |____V||  |  || \ / |    |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
                  |____V||  .  |                           _/ |  
                         |____V|                          |__/
    """
    print(ascii_art)

def limpiar_pantalla():
    # Comando para limpiar la pantalla en sistemas basados en Unix (Linux y macOS)
    if os.name == 'posix':
        os.system('clear')
    # Comando para limpiar la pantalla en sistemas basados en Windows
    elif os.name == 'nt':
        os.system('cls')

def imprimir_bienvenida():
    pass

# Assuming that we have an infinite deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # The value of 11 can change based on whether the result is above or below 21.
continuar = True

while continuar ==True:
    limpiar_pantalla()
    display_Ascii_art()
    imprimir_bienvenida()