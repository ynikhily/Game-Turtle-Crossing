# THIS FILE CONTAINS THE SCOREBOARD CLASS DEFINITION USED IN OUR PONG GAME
from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 280)
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"Game Over on Level {self.level}!!", font=FONT, align=ALIGN)

    def next_level(self):
        self.level += 1
        self.update_level()
