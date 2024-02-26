from turtle import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
segment = [0,0,0]

for positions in STARTING_POSITIONS:
    segment = Turtle('square')
    segment.color("white")
    segment.goto(positions)

screen.exitonclick()