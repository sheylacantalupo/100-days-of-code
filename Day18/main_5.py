from turtle import Turtle, Screen
from random import choice


tim = Turtle()
screen = Screen()
tim.speed("fastest")
angle = 0
colors = ["Indigo", "MediumPurple", "Purple", "DarkMagenta", "Fuchsia", "Violet", "Plum", "Orchid", "MediumOrchid",
          "DarkOrchid", "DarkViolet", "BlueViolet", "MediumSlateBlue"]  # Purple


for _ in range(100):
    tim.color(choice(colors))
    tim.setheading(angle)
    tim.circle(100)
    angle += 3.6

screen.exitonclick()