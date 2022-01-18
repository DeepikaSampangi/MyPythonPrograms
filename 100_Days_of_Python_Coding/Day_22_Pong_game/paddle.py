from mimetypes import init
from turtle import Turtle


UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle:
    def __init__(self) -> None:
        self.paddles = []
        self.create_paddles()
        self.player = self.paddles[0]

    def create_paddles(self):
        X_CORR = 350
        for i in range(2):
            self.paddles.append(Turtle())
            self.paddles[i].shape("square")
            self.paddles[i].penup()
            self.paddles[i].shapesize(stretch_len=1, stretch_wid=5)
            self.paddles[i].color("white")
            self.paddles[i].goto(X_CORR, 0)
            self.paddles[i].speed("fastest")
            X_CORR *= -1

    def up(self):
        self.player.setheading(UP)
        self.player.forward(MOVE_DISTANCE)

    def down(self):
        self.player.setheading(DOWN)
        self.player.forward(MOVE_DISTANCE)
