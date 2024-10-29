import random

# Diccionario de términos para estudiar para mi examen de master
terms = {
    "Shrank": "Simple past of Shrink",
    "Chose": "Simple past of Choose",
    "Dug": "Simple past of Dig",
    "Stole": "Simple past of Steal",
    "Withdrawn": "Past participle of Withdraw",
    "Forbidden": "Past participle of Forbid",
    "Shrunk": "Past participle of Shrink",
    "Wept": "Past participle of Weep",
    "Fled": "Past participle of Flee",
    "Begun": "Past participle of Begin",
    "Chosen": "Past participle of Choose",
    "Dug": "Past participle of Dig",
    "Forgiven": "Past participle of Forgive",
    "Spoken": "Past participle of Speak",
    "Stolen": "Past participle of Steal",
    "Swearing": "Gerund of Swear",
    "Withdrawing": "Gerund of Withdraw",
    "Shrinking": "Gerund of Shrink",
    "Weeping": "Gerund of Weep",
    "Bidding": "Gerund of Bid",
    "Dully": "De manera aburrida",
    "Greedily": "With excessive desire for more than is needed.",
    "Juggling": "Hacer malabares",
    "Sew": "Coser",
    "Backflip": "Hacer una voltereta hacia atrás",
    "Beat around the bush": "To avoid getting to the point.",
    "Every cloud has a silver lining": "Every difficult situation has a positive side or benefit.",
    "Skydive": "Jump out of a plane with a parachute",
    "Swore": "Simple past of Swear",
    "Withdrew": "Simple past of Withdraw",
    "Forbade": "Simple past of Forbid",
    "Wept": "Simple past of Weep",
    "Bid": "Simple past of Bid",
    "Fled": "Simple past of Flee",
    "Forbidding": "Gerund of Forbid",
    "Fleeing": "Gerund of Flee",
    "Began": "Simple past of Begin",
    "Sworn": "Past participle of Swear",
    "Bid": "Past participle of Bid",
    "Beginning": "Gerund of Begin",
    "Loosely": "Indicates an action done in a relaxed or uncontrolled manner",
    "Knit": "Tejer",
    "Hit the nail on the head": "To say something exactly right or to identify the main point or problem accurately.",
    "Inject": "Inyectar",
    'Bladder': 'Vejiga',
    'Liver': 'Higado',
    'Lungs': 'Pulmones',
    'Kidneys': 'Riñones',
    'Fair': 'Feria',
    'Plaza': 'Plaza',
    'Butcher Shop': 'Carnicería'
}

# Nuevos términos para el diccionario
terms.update({
    # Términos Principales
    "Father": "Who is the man who raised me?",
    "Mother": "Who is the woman who raised me?",
    "Brother": "What is a male sibling called?",
    "Sister": "What is a female sibling called?",
    "Son": "What do I call my male child?",
    "Daughter": "What do I call my female child?",
    "Husband": "Who is the man I am married to?",
    "Wife": "Who is the woman I am married to?",
    
    # Términos Extendidos
    "Grandfather": "Who is my father’s or mother’s father?",
    "Grandmother": "Who is my father’s or mother’s mother?",
    "Grandson": "If my child has a son, what is he to me?",
    "Granddaughter": "If my child has a daughter, what is she to me?",
    "Uncle": "Who is my parent's brother?",
    "Aunt": "Who is my parent's sister?",
    "Nephew": "What do I call my sibling's son?",
    "Niece": "What do I call my sibling's daughter?",
    "Cousin": "What do I call my aunt's or uncle's child?",
    
    # Familia por Matrimonio
    "Father-in-law": "Who is my spouse’s father?",
    "Mother-in-law": "Who is my spouse’s mother?",
    "Son-in-law": "Who is my daughter's husband?",
    "Daughter-in-law": "Who is my son's wife?",
    "Brother-in-law": "Who is my spouse’s brother?",
    "Sister-in-law": "Who is my spouse’s sister?",
    
    # Familia Mixta
    "Stepfather": "Who is my mother’s second husband?",
    "Stepmother": "Who is my father’s second wife?",
    "Stepson": "Who is my spouse’s son from another relationship?",
    "Stepdaughter": "Who is my spouse’s daughter from another relationship?",
    "Half-brother": "What do I call a brother with whom I share one parent?",
    "Half-sister": "What do I call a sister with whom I share one parent?",
    "Stepbrother": "Who is the son of my step-parent?",
    "Stepsister": "Who is the daughter of my step-parent?",
    
    # Familia por Adopción
    "Adoptive Father": "Who is the man who adopted me?",
    "Adoptive Mother": "Who is the woman who adopted me?",
    "Adoptive Parents": "Who are the people who adopted me?",
    "Foster Father": "Who is a man temporarily taking care of me?",
    "Foster Mother": "Who is a woman temporarily taking care of me?",
    "Foster Siblings": "Who are the other children living in my foster family?",
    
    # Familia en General y Extensa
    "Ancestor": "Who is a relative from a previous generation?",
    "Descendant": "Who is a relative from a future generation?",
    "Relative": "What do I call anyone related to me by blood or marriage?",
    "In-laws": "What do I call my spouse’s family members?",
    "Immediate Family": "Who are my parents and siblings collectively called?",
    "Extended Family": "Who are my relatives beyond my immediate family?"
})


def quiz_game():
    score = 0
    def_list = list(terms.items())  # Crea una lista de tuplas (término, definición)
    random.shuffle(def_list)  # Mezcla las definiciones

    print("¡Bienvenido al juego de términos! Trata de adivinar el término correcto para cada definición.")
    print("Escribe 'salir' en cualquier momento para terminar el juego.\n")

    for term, definition in def_list:  # Desempaqueta la tupla
        print(f"¿Cuál es el término para: '{definition}'?")  # Muestra la definición
        answer = input("Tu respuesta: ").strip()  # Pide al usuario que ingrese el término

        if answer.lower() == 'salir':
            break
        elif answer.lower() == term.lower():  # Compara con el término (key)
            print("¡Correcto!\n")
            score += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {term}\n")  # Muestra la respuesta correcta

    print(f"Juego terminado. Obtuviste {score} de {len(def_list)} términos correctos.")

# Ejecutar el juego
quiz_game()
