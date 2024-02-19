# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

# Challenge: Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

from turtle import *

COLORS = ['lightpink', 'lightblue', 'lightgreen', 'peachpuff', 'thistle', 'lightcoral', '#B2B9BF', '#709A86']

my_turtle = Turtle()

my_turtle.penup()
my_turtle.goto(40, 200)
my_turtle.pendown()

my_turtle.shape("turtle")
my_turtle.width(2)

for lados in range(3,11):
    my_turtle.color(COLORS[lados-3])
    grados = 360/lados
    for _ in range(lados):
        my_turtle.right(grados)
        my_turtle.forward(100)

screen = Screen()
screen.exitonclick()