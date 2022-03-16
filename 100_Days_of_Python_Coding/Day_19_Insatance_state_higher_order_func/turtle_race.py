import random
import turtle
from turtle import Screen, Turtle, width

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
        if turtle.xcor() > 230:
            is_race_on = False
            win_col = turtle.pencolor()
            if win_col == user_bet:
                print(f"You guessed it right, {win_col} Turtle won")
            else:
                print(f"Oops you were wrong, {win_col} Turtle won")

screen.exitonclick()
