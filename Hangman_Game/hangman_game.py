# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

# Credits for ASCII Art
# Hangman drawings: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
# Hangman Word: https://ascii.co.uk/art/hangman

import random

BANDAS_KPOP = [
    'bts', 'blackpink', 'exo', 'twice', 'got7', 'red velvet', 'nct', 'monsta x',
    'stray kids', 'itzy', 'ateez', 'izone', 'mamamoo', 'seventeen', 'x1', 'gfriend',
    'super junior', 'apink', 'momoland', 'vixx', 'btob', 'ab6ix', 'astro', 'oh my girl',
    'txt', 'everglow', 'kard', 'pentagon', 'oneus', 'chungha', 'iu', 'taemin', 'sunmi',
    'dreamcatcher', 'cix', 'wjsn', 'sf9', 'the boyz', 'loona', 'gidle', 'nuest',
    'golden child', 'weeekly', 'rocket punch', 'onf', 'fromis 9', 'cravity', 'above us',
    'lunarsolar', 't1419', 'stayc', 'enhypen', 'brave girls', 'woodz', 'weeekly', 'new jeans',
    'ive', 'le sserafim', 'sistar', 'hyolyn', 'itzy', 'nmixx', 'bangtan'
]

HANGMAN_PICS = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    /|\\  |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    /|\\  |
    /    |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    /|\\  |
    / \\  |
        |
    =========
    '''
]


def print_hangman_word():
    ascii_art = '''
    _
    | |
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
    | '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |
                    |___/
    '''
    print(ascii_art)


def print_hangman(errores):
    print(HANGMAN_PICS[errores])


def generar_palabra():
    return random.choice(BANDAS_KPOP)


def generar_censura(censura, posiciones, letra):
    for posicion in posiciones:
        if 0 <= posicion < len(censura):
            censura[posicion] = letra
    return censura


def encontrar_letra_posiciones(letra, cadena):
    posiciones = [pos for pos, char in enumerate(cadena) if char == letra]
    return posiciones

def contar_letras_numeros_unicos(cadena):
    caracteres_unicos = set(caracter for caracter in cadena if caracter.isalnum())
    return len(caracteres_unicos)

def preguntar_si_jugar_de_nuevo():
    while True:
        jugar_de_nuevo = input('¿Jugar de nuevo? (s/n): ').lower()
        if jugar_de_nuevo in ('s', 'si', 'sí', 'claro'):
            return True
        elif jugar_de_nuevo in ('n', 'no'):
            return False
        else:
            print("Respuesta no válida. Ingresa 's' para sí o 'n' para no.")


while True:
    aciertos = 0
    errores = 0
    active_game = True
    print_hangman_word()
    palabra_secreta = generar_palabra()
    lista_censurada = [' __ ' if caracter.isalnum() else caracter for caracter in palabra_secreta]
    palabra_censurada = ''.join(lista_censurada)

    print('¡Bienvenido a una nueva partida!')
    print('Intenta averiguar la palabra: ')
    print(palabra_censurada)
    print_hangman(errores)

    while active_game:
        while True:
            input_letra = input('Ingresa una letra: ').lower()
            if input_letra.isalnum() and len(input_letra) == 1:
                break
            else:
                print("Por favor, ingresa una letra.")

        if input_letra in palabra_secreta:
            aciertos += 1
            lista_posiciones = encontrar_letra_posiciones(input_letra, palabra_secreta)
            lista_censurada = generar_censura(lista_censurada, lista_posiciones, input_letra)
            palabra_censurada = ''.join(lista_censurada)

            if aciertos == contar_letras_numeros_unicos(palabra_secreta):
                active_game = False
                print('\n¡Ganaste el juego!')
                print(f'La palabra secreta es: {palabra_secreta}')
            else:
                print(palabra_censurada)
        else:
            errores += 1
            if errores > 5:
                print_hangman(errores)
                print('\n¡Perdiste el juego!')
                print(f'La palabra secreta era: {palabra_secreta}')
                active_game = False
            else:
                print_hangman(errores)
                print(palabra_censurada)

    if not preguntar_si_jugar_de_nuevo():
        break