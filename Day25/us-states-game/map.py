from turtle import Turtle
import pandas

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()


class States(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.states_list = data["state"].to_list()
        self.guessed_states = []
        self.states_learn = []

    def guess_is_among(self, answer):
        if answer in self.states_list:
            cor = data[data.state == answer]
            self.penup()
            self.goto(int(cor.x), int(cor.y))
            self.write(f"{answer}", align=ALIGNMENT, font=FONT)
            self.guessed_states.append(answer)

    def states_to_learn(self):

        self.states_learn = [state for state in self.states_list if state not in self.guessed_states]
        print(self.states_learn)
        new_data = pandas.DataFrame(self.states_learn)
        new_data.to_csv("states_to_learn.csv")









