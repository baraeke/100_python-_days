import turtle
import pandas

FONT = ("Courier", 16, "bold")
correct_guess = 0
guessed_states = []

# Screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
map_image = "blank_states_img.gif"
screen.addshape(map_image)
turtle.shape(map_image)

# Scoreboard turtle
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()

# Read states data
data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].tolist()

# Game loop
while len(guessed_states) < len(list_of_states):
    answer_state = screen.textinput(
        title=f"{correct_guess}/{len(list_of_states)} States Correct",
        prompt="What's another state's name? (or type 'Exit' to quit)"
    )
    
    if not answer_state:
        continue
    
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in list_of_states and answer_state not in guessed_states:
        state_data = data[data.state == answer_state]
        xcor, ycor = int(state_data.x), int(state_data.y)
        scoreboard.pencolor("green")
        scoreboard.goto(x=xcor, y=ycor)
        scoreboard.write(answer_state, align="center", font=FONT)
        guessed_states.append(answer_state)
        correct_guess += 1

# Game Over Message
scoreboard.goto(0, 0)
if len(guessed_states) == len(list_of_states):
    scoreboard.write("YOU DID IT!", align="center", font=("Courier", 20, "bold"))
    scoreboard.goto(0, -30)
    scoreboard.write("You guessed all states right!", align="center", font=FONT)
else:
    scoreboard.write("YOU QUIT!", align="center", font=("Courier", 20, "bold"))
    scoreboard.goto(0, -30)
    scoreboard.write(f"You guessed {correct_guess} states.", align="center", font=FONT)

# Offer to show unguessed states
if screen.textinput(title="Review", prompt="View unguessed states? Type 'yes' to view:").lower() == "yes":
    states_to_learn = [state for state in list_of_states if state not in guessed_states]
    for state in states_to_learn:
        state_data = data[data.state == state]
        xcor, ycor = int(state_data.x), int(state_data.y)
        scoreboard.pencolor("red")
        scoreboard.goto(xcor, ycor)
        scoreboard.write(state, align="center", font=("Courier", 10, "normal"))

    # Save unguessed states
    data_dict = {
        "state": states_to_learn,
        "x": [int(data[data.state == s].x) for s in states_to_learn],
        "y": [int(data[data.state == s].y) for s in states_to_learn]
    }
    pandas.DataFrame(data_dict).to_csv("states_to_learn.csv", index=False)

screen.exitonclick()
