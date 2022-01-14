from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("red")


def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


draw_square()

screen = Screen()
screen.exitonclick()
