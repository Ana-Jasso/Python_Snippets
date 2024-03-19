from turtle import *

COLOR = 'white'
SHAPE = 'square'
STEPS = 15
STCH_WID = 5
STCH_LEN = 1

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.shapesize(stretch_wid=STCH_WID, stretch_len=STCH_LEN)
        self.penup()
        self.goto(x_pos,y_pos)
    
    def move_up(self):
        new_y = self.ycor() + STEPS
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - STEPS
        self.goto(self.xcor(), new_y)