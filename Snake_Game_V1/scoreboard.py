from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,260)
        self.score = 0
        self.show_scoreboard()
    
    def increase_scoreboard(self):
        self.score += 1
        self.show_scoreboard()
    
    def show_scoreboard(self):
        self.clear()
        self.text = f'Score: {self.score}'
        self.write(self.text, align="center", font=("Arcade Classic", 12, "normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write('Game Over.', align="center", font=("Arcade Classic", 12, "normal"))