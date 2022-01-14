import random
from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("red")

colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]


def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


# draw_square()


def dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


# dashed_line()


def draw_all_shapes():
    for i in range(3, 10):
        x = 360 / i
        for _ in range(i):
            tim.forward(100)
            tim.right(x)


# draw_all_shapes()


def random_walk():
    directions = [0, 90, 180, 270]
    tim.pensize(15)
    tim.speed("fastest")
    for _ in range(200):
        tim.color(random.choice(colours))
        tim.forward(30)
        tim.setheading(random.choice(directions))


# random_walk()


screen = Screen()
screen.exitonclick()
