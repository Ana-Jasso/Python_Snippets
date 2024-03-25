# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.
# Instead of increasing the speed by 10 every time the player scores a point, I decided to increase it by 2 and adjust the frequency of creating cars so that they are generated a little faster compared to the first 3 rounds.

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,'Up')

game_is_on = True
loop = 0
NUM_LIMIT = 6

while game_is_on:
    time.sleep(0.09)
    if (loop == 0) or (loop % NUM_LIMIT == 0):
        car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.cars:
        if player.distance(car)<20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() >= 280:
        scoreboard.score_a_point()
        player.star_over()
        car_manager.speed += 2
        if NUM_LIMIT > 3:
            NUM_LIMIT -= 1
    screen.update()
    loop += 1

screen.exitonclick()