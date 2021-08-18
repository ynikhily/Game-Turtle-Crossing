# THIS IS THE DEFINITION OF OUR TURTLE PLAYER WHICH IS TRYING TO CROSS THE ROAD.
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.goto(0, -270)

    def move_up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.goto(0, -270)
