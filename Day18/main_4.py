from turtle import Turtle, Screen
from random import choice, randint
import turtle as t

tim = Turtle()
screen = Screen()
tim.speed("fastest")
t.colormode(255)
tim.pensize(15)
colors = ["Indigo", "MediumPurple", "Purple", "DarkMagenta", "Fuchsia", "Violet", "Plum", "Orchid", "MediumOrchid",
          "DarkOrchid", "DarkViolet", "BlueViolet", "MediumSlateBlue"]  # Purple
directions = [0, 90, 180, 270]


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(200):
    tim.color(random_color())
    tim.setheading(choice(directions))
    tim.forward(30)

screen.exitonclick()