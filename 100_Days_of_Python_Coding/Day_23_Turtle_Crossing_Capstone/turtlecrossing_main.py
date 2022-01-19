import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

scoreboard = Scoreboard()

cars = CarManager()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.5)
    screen.update()
    # Detect Reach to the end
    if player.ycor() > 275:
        scoreboard.level += 1
        player.reset()
        scoreboard.updated_score()
    cars.initialize_cars()
    cars.move_cars()

screen.exitonclick()
