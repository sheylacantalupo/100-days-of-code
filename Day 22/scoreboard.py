from turtle import Turtle
from ball import Ball

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class ScoreBoard(Turtle):

    def __init__(self, x):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x, 200)
        self.update()

    def update(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        pass
