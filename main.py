import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# ---------------------------------------------SCREEN SETUP-----------------------------------------------
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# -----------INITIALISATION OF PLAYER, CAR MANAGER FOR CARS AND SCOREBOARD FOR OUR GAME-----------------
player = Player()
cars = CarManager()
level = Scoreboard()
game_is_on = True

# ---------------------------------KEY BINDING FOR TURTLE'S MOVEMENT--------------------------------------
screen.listen()
screen.onkeypress(fun=player.move_up, key='w')
collision = 0

# ---------------------------------------GAME FLOW BEGINS--------------------------------------------------
while game_is_on:
    cars.move_car()
    cars.update_car()
    time.sleep(0.1)
    for car in cars.car_list:
        if player.distance(car) < 20:
            game_is_on = False
    if player.ycor() > 270:
        player.refresh()
        cars.level_up()
        level.next_level()

    screen.update()

level.game_over()
screen.exitonclick()
