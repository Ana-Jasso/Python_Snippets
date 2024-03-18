from turtle import *

COLOR = 'white'
SHAPE = 'square'

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos,y_pos)
    
    def move_up(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 15
        self.goto(self.xcor(), new_y)