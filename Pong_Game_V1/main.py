# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

from turtle import *
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle(x_pos=350, y_pos=0)
left_paddle = Paddle(x_pos=-350, y_pos=0)
ball = Ball(x_pos=0, y_pos=0)

screen.listen()
screen.onkeypress(right_paddle.move_up, 'Up')
screen.onkeypress(right_paddle.move_down, 'Down')
screen.onkeypress(left_paddle.move_up, 'w')
screen.onkeypress(left_paddle.move_down, 's')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()