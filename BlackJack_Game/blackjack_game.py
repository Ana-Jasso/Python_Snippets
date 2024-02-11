# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

# Credits for ASCII Art
# Text: https://ascii.co.uk/art/blackjack
# Draw: https://www.asciiart.eu/miscellaneous/playing-cards

import os
import random

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

def imprimir_bienvenida(cartas_jugador, carta_computadora):
    print('¡Bienvenido a una nueva partida!')
    print(f'Tus cartas son: {cartas_jugador}')
    print(f'La primera carta de tu oponente es: {carta_computadora}')

def generar_cartas(cards):
    cartas = random.sample(cards, 2)
    return cartas

def evaluar_eleccion(eleccion, players_cards):
    if eleccion.lower() in ['yes', 'y', 'sure']:
        players_cards.append(random.choice(cards))
    return players_cards

def evaluar_ganador(players_cards, computer_cards):
    suma_jugador = sum(players_cards)
    suma_computadora = sum(computer_cards)
    if suma_jugador > 21:
        print(f'La suma de tus cartas es de {suma_jugador}, por lo tanto tu perdiste.')
    else:
        if suma_computadora > suma_computadora:
            print('¡Ganaste!')
            print(f'La suma de tus cartas es de {suma_jugador} y la de tu oponente es de {suma_computadora}.')
        elif suma_computadora == suma_computadora:
            print('¡Empate!')
            print(f'La suma de ambos es de {suma_jugador}, por lo tanto es un empate.')
        else:
            print('¡Perdiste!')
            print(f'La suma de tus cartas es de {suma_jugador} y la de tu oponente es de {suma_computadora}.')

# Assuming that we have an infinite deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # The value of 11 can change based on whether the result is above or below 21.
continuar = True

while continuar == True:
    limpiar_pantalla()
    display_Ascii_art()
    #Generando las cartas
    players_cards = generar_cartas(cards)
    computer_cards = generar_cartas(cards)
    #Imprimir información
    imprimir_bienvenida(players_cards, computer_cards[0])
    
    eleccion_jugador = input('Ingresa "y" para obtener otra carta o "n" para pasar: ')

    while eleccion_jugador.lower() not in ['yes', 'y', 'no', 'n', 'sure']:
        print("Please enter a valid response (y/n).")
        eleccion_jugador = input('Ingresa "y" para obtener otra carta o "n" para pasar: ')
    
    players_cards = evaluar_eleccion(eleccion_jugador, players_cards)

    print(f'Tu mazo final: {players_cards}')
    print(f'El mazo final de tu oponente: {computer_cards}')

    evaluar_ganador(players_cards, computer_cards)

    seguir_jugando = input('¿Quieres seguir jugando? (y/n): ')
    while seguir_jugando.lower() not in ['yes', 'y', 'no', 'n', 'sure']:
        print("Please enter a valid response (y/n).")
        seguir_jugando = input('¿Quieres seguir jugando? (y/n): ')
    
    if seguir_jugando not in ['yes', 'y', 'sure']:
        continuar = False