from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

def draw_square():
    for _ in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)

draw_square()

screen = Screen()
screen.exitonclick()
