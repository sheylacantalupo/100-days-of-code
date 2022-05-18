from turtle import Turtle, Screen

tim = Turtle()
colors = ["blue", "yellow", "red", "green", "pink", "brown", "orange", "purple"]
i = 0


def cal_angle(side):
    angle = 360 / side
    return angle


for sides in range(3, 11, 1):  # sides
    tim.color(colors[i])
    for _ in range(sides):
        tim.forward(100)
        tim.right(cal_angle(sides))
    i += 1

screen = Screen()
screen.exitonclick()
