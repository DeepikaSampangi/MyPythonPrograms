from turtle import Screen, Turtle, position
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for pos in starting_position:
    new_seg = Turtle(shape="square")
    new_seg.color("white")
    new_seg.penup()
    new_seg.goto(pos)
    segments.append(new_seg)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.5)

    for seg_num in range(len(starting_position) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
