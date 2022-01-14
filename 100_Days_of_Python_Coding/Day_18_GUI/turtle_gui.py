import random
from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("red")


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
    directions = [tim.forward(50), tim.backward(50), tim.right(50), tim.left(50)]
    for _ in range(100):
        random.choice(directions)


random_walk()


screen = Screen()
screen.exitonclick()
