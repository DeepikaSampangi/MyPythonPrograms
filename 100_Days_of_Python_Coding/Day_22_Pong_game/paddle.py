from mimetypes import init
from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(position)
        self.speed("fastest")

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y < 275:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y > -275:
            self.goto(self.xcor(), new_y)
