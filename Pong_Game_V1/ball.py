from turtle import *

COLOR = 'blue'
SHAPE = 'circle'
STCH_WID = 1
STCH_LEN = 1

class Ball(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        #self.shapesize(stretch_wid=, stretch_len=)
        self.penup()
        self.goto(x_pos,y_pos)
    pass