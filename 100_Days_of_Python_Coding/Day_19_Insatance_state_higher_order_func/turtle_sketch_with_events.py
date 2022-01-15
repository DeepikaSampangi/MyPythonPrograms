from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fwds():
    tim.forward(10)


def move_bkwd():
    tim.backward(10)


def move_right():
    tim.right(10)


def move_left():
    tim.left(10)


screen.listen()
screen.onkey(key="w", fun=move_fwds)
screen.onkey(key="s", fun=move_bkwd)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)

screen.exitonclick()
