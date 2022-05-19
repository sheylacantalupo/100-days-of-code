from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "blue", "green", "yellow", "purple"]
turtles = []
y = -100
for _ in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[_])
    turtle.penup()
    turtle.goto(-230, y)
    turtles.append(turtle)
    y += 44

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        random_forward = randint(0, 10)
        turtle.forward(random_forward)


