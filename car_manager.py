# THIS FILE DEFINES THE CAR MANAGER CLASS THAT IS RESPONSIBLE FOR SPAWNING CARS FOR OUR GAME.
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.car_list = []
        for _ in range(25):
            x = random.randint(-280, 280)
            y = random.randint(-240, 240)
            self.generate_car(x, y)
            self.move_distance = 5

    def generate_car(self, x, y):
        car = Turtle('square')
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.goto(x, y)
        self.car_list.append(car)

    def move_car(self):
        for car in self.car_list:
            car.forward(self.move_distance)

    def update_car(self):
        for car in self.car_list:
            if car.xcor() < -280:
                x = random.randint(300, 350)
                y = random.randint(-250, 250)
                car.goto(x, y)

    def level_up(self):
        self.move_distance += 5
