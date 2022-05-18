from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

colors = ["red", "blue", "black", "pink"]
for _ in range(4):
    color = colors[_]
    tim.color(color)
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()