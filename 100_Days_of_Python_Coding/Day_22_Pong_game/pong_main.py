from turtle import Screen, Turtle, position
from paddle import Paddle
from ball import PongBall
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))

pong_ball = PongBall()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.01)
    pong_ball.move()
    screen.update()

    # Detect Wall Collision
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce()

screen.exitonclick()
