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


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.initialize_cars()
    cars.move_cars()

    # Detect Reach to the end
    if player.ycor() > 275:
        scoreboard.level += 1
        player.reset()
        scoreboard.updated_score()

    # Detect car collision
    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False

screen.exitonclick()
