from turtle import *

COLOR = 'blue'
SHAPE = 'turtle'
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        pass
    def move(self):
        self.forward(MOVE_DISTANCE)