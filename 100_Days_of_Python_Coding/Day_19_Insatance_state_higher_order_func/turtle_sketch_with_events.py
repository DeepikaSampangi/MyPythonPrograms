from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fwds():
    tim.forward(20)


def move_bkwd():
    tim.backward(20)


def turn_right():
    tim.right(90)


def turn_left():
    tim.left(90)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_fwds)
screen.onkey(key="s", fun=move_bkwd)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
