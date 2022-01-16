import imp
from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
SNAKE_SHAPE = "square"


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            new_seg = Turtle(shape=SNAKE_SHAPE)
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(pos)
            self.segments.append(new_seg)

    def move_snake(self):
        for seg_num in range(len(STARTING_POSITIONS) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIST)
