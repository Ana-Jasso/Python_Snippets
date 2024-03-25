# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

from turtle import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while(game_is_on):
    screen.update()
    time.sleep(0.08)
    snake.move()
    
    # Detect collison with food.
    if snake.head.distance(food)<16:
        food.refresh()
        scoreboard.increase_scoreboard()
        snake.grow()

    # Detect collison with wall.
    if (snake.head.xcor() > 290) or (snake.head.xcor() < -290) or (snake.head.ycor() > 290) or (snake.head.ycor() < -290):
        scoreboard.game_over()
        game_is_on = False

    # Detect collison with snake.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()