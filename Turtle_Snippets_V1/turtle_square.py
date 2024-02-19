# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

from turtle import *

my_turtle = Turtle()

for _ in range(4):
    my_turtle.right(90)
    for _ in range(10):
        my_turtle.forward(10)
        my_turtle.penup()
        my_turtle.forward(10)
        my_turtle.pendown()

screen = Screen()
screen.exitonclick()