from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()


def move_fwds():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_fwds)

screen.exitonclick()
