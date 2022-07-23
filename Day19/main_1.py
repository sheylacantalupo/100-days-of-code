from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def turn_left():
    heading = tim.heading() + 10
    tim.setheading(heading)


def turn_right():
    heading = tim.heading() - 10
    tim.setheading(heading)


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def clear_drawing():
    tim.goto(0, 0)
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()