# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

from turtle import *
import random

COLORS = ['#964083', '#C572A5',  '#EAB8D9', '#B2B9BF', '#709A86', '#40cfff'] # '#E38C24',
SPEED = 100
CIRCLES_RADIO = 100

my_turtle = Turtle()

my_turtle.shape("turtle")
my_turtle.width(1.1)
my_turtle.speed(SPEED)

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        my_turtle.color(COLORS[i % len(COLORS)])
        my_turtle.circle(CIRCLES_RADIO)
        my_turtle.setheading(my_turtle.heading()+size_of_gap)

draw_spirograph(3)

screen = Screen()
screen.exitonclick()