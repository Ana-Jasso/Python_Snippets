from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,260)
        self.score = 0
        self.highscore = 0
        self.show_scoreboard()
    
    def increase_scoreboard(self):
        self.score += 1
        self.show_scoreboard()
    
    def show_scoreboard(self):
        self.clear()
        self.text = f'Score: {self.score}         High Score:{self.highscore}'
        self.write(self.text, align="center", font=("Arcade Classic", 12, "normal"))
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.show_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('Game Over.', align="center", font=("Arcade Classic", 12, "normal"))