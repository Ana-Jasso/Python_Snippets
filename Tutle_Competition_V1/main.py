# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

from turtle import *
import random

POSICIONES_Y = [-70, -40, -10, 20, 50, 80]
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

screen = Screen()
screen.setup(width=500, height=400)

# Input del usuario
user_bet = screen.textinput(title="BET", prompt="Who's gonna win? Name a color:")
while user_bet not in COLORS:
    user_bet = screen.textinput(title="BET", prompt="Who's gonna win? Name a color:")
print(f'Your bet: {user_bet}.')

#Crear tortugas
for i in range(len(COLORS)):
    turtles.append(Turtle())
    turtles[i].color(COLORS[i])
    turtles[i].name = COLORS[i]
    turtles[i].shape('turtle')
    turtles[i].penup()
    turtles[i].goto(x=-230, y=POSICIONES_Y[i])

# Iniciando la carrera
nadie_ha_ganado = True
while nadie_ha_ganado:
    tortuga_a_mover = random.randint(0, 5)
    turtles[tortuga_a_mover].forward(random.randint(0, 15))
    if turtles[tortuga_a_mover].xcor() >= 250:
        nadie_ha_ganado = False
        winner = turtles[tortuga_a_mover].name
        if winner == user_bet:
            print(f'You win! The winner is {winner}.')
        else:
            print(f'You lose! The winner is {winner}.')

screen.exitonclick()