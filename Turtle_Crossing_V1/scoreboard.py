from turtle import *

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-200,260)
        self.score = 0
        self.show_scoreboard()
    
    def show_scoreboard(self):
        self.clear()
        self.text = f'Score: {self.score}'
        self.write(self.text, align="center", font=FONT)
    
    def score_a_point(self):
        self.score += 1
        self.show_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.text = 'Game Over'
        self.write(self.text, align="center", font=FONT)