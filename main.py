import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

ALL_STATES = 50
found_states = 0

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
guessed_states = []


def print_turtle(state, x_cor, y_cor):
    state_turtle = turtle.Turtle()
    state_turtle.hideturtle()
    state_turtle.penup()
    state_turtle.speed(0)
    state_turtle.color("black")
    state_turtle.goto(x_cor, y_cor)
    state_turtle.write(f"{state}", align="center", font=("Arial", 5, "bold"))


def game_over():
    game_over_turtle = turtle.Turtle()
    game_over_turtle.hideturtle()
    game_over_turtle.penup()
    game_over_turtle.speed(0)
    game_over_turtle.color("black")
    game_over_turtle.goto(0, 0)
    game_over_turtle.write("You won !", align="center", font=("Arial", 60, "bold"))


game_is_on = True
while game_is_on:
    guess = screen.textinput(f"{found_states}/{ALL_STATES} states found", "What's another state name?").title()
    if guess == "Exit":
        break
    if guess in state_list and guess not in guessed_states:
        state_data = data[data.state == guess]
        print_turtle(guess, int(state_data.x), int(state_data.y))
        found_states += 1
        guessed_states.append(guess)
    if found_states == 50:
        game_over()
        game_is_on = False

states_to_learn = [state for state in state_list if state not in guessed_states]
df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")



