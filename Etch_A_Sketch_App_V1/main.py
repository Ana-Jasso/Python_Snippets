# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

from turtle import *

def walk_forward():
    my_turtle.forward(PASOS)

def walk_backward():
    my_turtle.backward(PASOS)

def turn_Counter_Clockwise():
    my_turtle.left(ANGULO_DE_GIRO)

def turn_Clockwise():
    my_turtle.right(ANGULO_DE_GIRO)

def clear_all():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

PASOS = 25
ANGULO_DE_GIRO = 10

my_turtle = Turtle()
my_turtle.shape('turtle')
my_turtle.color('purple')
my_turtle.speed(80)

screen = Screen()
screen.listen()
screen.onkey(walk_forward,'w')
screen.onkey(walk_backward,'s')
screen.onkey(turn_Counter_Clockwise,'a')
screen.onkey(turn_Clockwise,'d')
screen.onkey(clear_all,'c')
screen.exitonclick()