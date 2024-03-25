from turtle import *
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SHAPE = 'square'
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STCH_WID = 1
STCH_LEN = 2

class CarManager():
    def __init__(self):
        super().__init__()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape(SHAPE)
        car.shapesize(stretch_wid=STCH_WID, stretch_len=STCH_LEN)
        car.color(random.choice(COLORS))
        car.goto(350,random.randint(-250, 250))
        car.setheading(180)
        car.forward(self.speed)
        self.cars.append(car)
    
    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)