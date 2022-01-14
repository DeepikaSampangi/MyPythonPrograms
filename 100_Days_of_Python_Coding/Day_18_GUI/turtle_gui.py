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

screen = Screen()
screen.exitonclick()
