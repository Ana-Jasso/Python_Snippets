# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

from turtle import *
import random

COLORS = ['#964083', '#C572A5', '#E38C24', '#EAB8D9', '#B2B9BF', '#709A86']
GRADOS_PREDETERMINADOS = [0, 90, 180, 270]

my_turtle = Turtle()

my_turtle.shape("turtle")
my_turtle.width(11)
speed = 5
for i in range(450):
    color = random.choice(COLORS)
    my_turtle.color(color)

    grados = random.choice(GRADOS_PREDETERMINADOS)
    my_turtle.setheading(grados)

    my_turtle.forward(20)
    if i % 10 == 0:
        speed += 20
    my_turtle.speed(speed)

screen = Screen()
screen.exitonclick()