from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

data = open("data.txt")
current = int(data.read())


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = current
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()


