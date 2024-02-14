# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

# Credits for ASCII Art
# Text: https://patorjk.com/software/taag/#p=display&f=Big&t=Number%20Guessing%20Game 

import random
import os

def print_ASCII():
    ascii_art = '''
  _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \ 
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                    
    '''
    print(ascii_art)

def limpiar_pantalla():
    # Comando para limpiar la pantalla en sistemas basados en Unix (Linux y macOS)
    if os.name == 'posix':
        os.system('clear')
    # Comando para limpiar la pantalla en sistemas basados en Windows
    elif os.name == 'nt':
        os.system('cls')

def evaluar_numero(guess, real):
    if guess > real:
        print('¡Muy alto!')
        return False
    elif guess < real:
        print('¡Muy bajo!')
        return False
    else:
        print('¡Has acertado!')
        return True

def jugar(attempts, numero):
    evaluacion = False
    while not evaluacion:
        if attempts > 0:
            print(f'You have {attempts} attempts remaining to guess the number.')
            try:
                input_user = int(input('Make a guess: '))
            except ValueError:
                print("Please enter a number.")
                continue

            evaluacion = evaluar_numero(input_user, numero)
            attempts -= 1
        else:
            print('Se acabaron los intentos.')
            break
    print(f'El número era: {numero}')

continuar = True

while continuar == True:
    limpiar_pantalla()
    print_ASCII()
    numero_aleatorio = random.randint(1, 100)

    seleccionar_dificultad = input('Elige la difficultad (hard/easy): ')
    while seleccionar_dificultad.lower() not in ['hard', 'easy']:
        print("Please enter a valid response (y/n).")
        seleccionar_dificultad = input('Elige la difficultad (hard/easy): ')
    
    if seleccionar_dificultad == 'hard':
        attempts = 5
    else:
        attempts = 10
    
    jugar(attempts, numero_aleatorio)

    seguir_jugando = input('¿Quieres seguir jugando? (y/n): ')
    while seguir_jugando.lower() not in ['yes', 'y', 'no', 'n', 'sure']:
        print("Please enter a valid response (y/n).")
        seguir_jugando = input('¿Quieres seguir jugando? (y/n): ')
    
    if seguir_jugando.lower() not in ['yes', 'y', 'sure']:
        continuar = False