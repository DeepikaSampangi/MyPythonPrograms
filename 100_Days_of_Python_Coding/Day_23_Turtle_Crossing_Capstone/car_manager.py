from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.cars = []

    def initialize_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6 or random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            new_car.setheading(180)

            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
