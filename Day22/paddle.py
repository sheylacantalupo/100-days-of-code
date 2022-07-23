from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(cor)

    def up(self):
        x = self.xcor()
        y = self.ycor()
        new_y = y + 20
        self.goto(x, new_y)

    def down(self):
        x = self.xcor()
        y = self.ycor()
        new_y = y - 20
        self.goto(x, new_y)

