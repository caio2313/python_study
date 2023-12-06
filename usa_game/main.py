import turtle
import pandas

data = pandas.read_csv("50_states.csv")
name = data["state"].to_list()
coord_x = data["x"]
coord_y = data["y"]
coord = [coord_x, coord_y]

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's").title()

    if answer_state == "Exit":
        break
    if answer_state in name:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

states_to_learn = []
for state in name:
    if state not in guessed_states:
        states_to_learn.append(state)

print(states_to_learn)
screen.exitonclick()
