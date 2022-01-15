from turtle import Turtle, Screen, width
import random
import turtle

colors = ["red", "orange", "green", "blue", "purple", "yellow"]
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

print(f"Turtle colors {colors}")
user_bet = screen.textinput(
    title="User Bet", prompt="Which turtle will win the race? Enter a color: "
)

turtle_list = []
y_cord = -125

for i in range(6):
    turtle_list.append(Turtle(shape="turtle"))
    turtle_list[i].color(colors[i])
    turtle_list[i].penup()
    turtle_list[i].goto(x=-230, y=y_cord)
    y_cord += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        random_direction = random.randint(0, 10)
        turtle.forward(random_direction)

screen.exitonclick()
