# import turtle

# timmy = turtle.Turtle()
# print(timmy)

from turtle import Screen, Turtle

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
