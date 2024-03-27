from turtle import *

data_file_name = 'Snake_Game_V2\data.txt'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,260)
        self.score = 0
        self.highscore = self.get_high_score()
        self.show_scoreboard()
    
    def increase_scoreboard(self):
        self.score += 1
        self.show_scoreboard()
    
    def show_scoreboard(self):
        self.clear()
        self.text = f'Score: {self.score}         Highest Score: {self.highscore}'
        self.write(self.text, align="center", font=("Arcade Classic", 12, "normal"))
    
    def reset(self):
        if self.score > self.highscore:
            with open (data_file_name, mode='w') as data:
                data.write(str(self.score))
        self.highscore = self.get_high_score()
        self.score = 0
        self.show_scoreboard()

    def get_high_score(self):
        with open (data_file_name, mode='r') as data:
            return int(data.read())