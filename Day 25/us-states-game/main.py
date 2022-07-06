import turtle
from map import States

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state = States()


while len(state.guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(state.guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    state.guess_is_among(answer_state)

    if answer_state == "Exit":
        state.states_to_learn()
        break


screen.exitonclick()