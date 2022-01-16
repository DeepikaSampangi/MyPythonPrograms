from turtle import Screen, Turtle, position

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]
for pos in starting_position:
    new_seg = Turtle(shape="square")
    new_seg.color("white")
    new_seg.goto(pos)

screen.exitonclick()
