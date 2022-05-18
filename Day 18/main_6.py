import turtle as turtle_module
from turtle import Turtle, Screen
from random import choice

turtle_module.colormode(255)
screen = Screen()
tim = Turtle()
tim.speed('fastest')
tim.hideturtle()
y = -200
color_list = [(236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35),
              (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195),
              (126, 193, 74), (253, 223, 0), (85, 28, 93)]


tim.penup()
tim.goto(-200, -200)
for _ in range(10):
    tim.goto(-200, y)
    for _ in range(10):
        color = choice(color_list)
        tim.dot(20, color)
        tim.forward(50)
    y += 50

screen.exitonclick()
