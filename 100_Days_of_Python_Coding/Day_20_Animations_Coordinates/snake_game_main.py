from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

start = 0
snake_list = []
for i in range(3):
    snake_list.append(Turtle(shape="square"))
    snake_list[i].color("white")
    snake_list[i].setx(start)
    start += 20

screen.exitonclick()
