from turtle import *
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
segments = []

for positions in STARTING_POSITIONS:
    segment = Turtle('square')
    segment.color("white")
    segment.penup()
    segment.goto(positions)
    segments.append(segment)

screen.update()

game_is_on = True
while(game_is_on):
    screen.update()
    for seg in segments:
        seg.forward(20)
        time.sleep(1)


screen.exitonclick()