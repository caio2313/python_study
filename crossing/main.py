import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.mov, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.car_move()

    for carro in car.all_cars:
        if carro.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()

screen.exitonclick()
