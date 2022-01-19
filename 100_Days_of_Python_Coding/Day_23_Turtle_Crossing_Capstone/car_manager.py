from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.cars = []

    def initialize_cars(self):
        for i in range(random.randint(1, 5)):
            self.cars.append(Turtle(shape="square"))
            self.cars[-1].shapesize(stretch_len=2, stretch_wid=1)
            self.cars[-1].color(random.choice(COLORS))
            self.cars[-1].penup()
            self.cars[-1].goto(310, random.randint(-280, 280))
            self.cars[-1].setheading(180)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
