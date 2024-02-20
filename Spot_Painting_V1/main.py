# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

from turtle import *
import random

def convert_color(rgb):
    return tuple(val / 255.0 for val in rgb)

COLORS = [(205, 157, 125), (227, 209, 189), (158, 75, 47), (52, 21, 10), (126, 36, 27), (180, 106, 87)]

my_turtle = Turtle()
my_turtle.hideturtle()
my_turtle.shape('turtle')
my_turtle.color('lightpink')
my_turtle.speed(50)

# Go to the starting Point, -340 is the limit for x 
x = -325 #Starting
y = -240 #Starting

columns = 9
rows = 7

SPACE_BETWEEN = 80
DOTS_SIZE = 15

my_turtle.penup()
my_turtle.goto(x, y)
my_turtle.pendown()

for j in range(rows):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    for i in range(columns):
        #my_turtle.dot(DOTS_SIZE, convert_color(COLORS[i % len(COLORS)]))
        my_turtle.dot(DOTS_SIZE, convert_color(random.choice(COLORS)))
        my_turtle.penup()
        my_turtle.forward(SPACE_BETWEEN) #blank space
        my_turtle.pendown()
    y += SPACE_BETWEEN

screen = Screen()
screen.exitonclick()