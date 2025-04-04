import turtle
import pandas

FONT = ("Courier", 16, "bold")
correct_guess = 0
guessed_states = []
wants_play_again = True

# Screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
map = "blank_states_img.gif"
screen.addshape(map)
turtle.shape(map)

scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()

data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].tolist()

i = 0
while i < len(list_of_states) and wants_play_again:
    answer_state = screen.textinput(title=f"{correct_guess}/{len(list_of_states)} States Correct", prompt="Make another guess or type 'Exit' to quit").title()
    
    if answer_state == "Exit":
        wants_play_again = False
        scoreboard.goto(x=0, y=0)
        scoreboard.write(arg=f"YOU QUITED", align="center", font=("Courier", 20, "bold"), move=False)
        scoreboard.goto(x=0, y=-30)
        scoreboard.write(arg=f"You were able to guess {correct_guess} states", align="center", font=("Courier", 16, "bold"), move=False)
        break
    
    if answer_state in list_of_states and answer_state not in guessed_states:
        state_data = data[data.state == answer_state]
        xcor = int(state_data["x"].iloc[0])
        ycor = int(state_data["y"].iloc[0])
        scoreboard.pencolor("green")
        scoreboard.goto(x=xcor, y=ycor)
        scoreboard.write(arg=f"{answer_state}", align="center", font=FONT, move=False)
        guessed_states.append(answer_state)
        correct_guess += 1
        i += 1
    
    if i == len(list_of_states):
        scoreboard.goto(x=0, y=0)
        scoreboard.write(arg=f"YOU DID IT", align="center", font=("Courier", 20, "bold"), move=False)
        scoreboard.goto(x=0, y=-30)
        scoreboard.write(arg=f"You guessed all states right", align="center", font=("Courier", 16, "bold"), move=False)


answer_state = screen.textinput(title=f"Do you want to view the unguessed states?", prompt="Enter 'yes' to view").lower()

states_to_learn = []
x = []
y = []
for state in list_of_states:
    if state not in guessed_states:
        state_data = data[data.state == state]
        states_to_learn.append(state)
        x.append(int(state_data["x"].iloc[0]))
        y.append(int(state_data["y"].iloc[0]))
        if answer_state == "yes":
            scoreboard.pencolor("red")
            scoreboard.goto(x=int(state_data["x"].iloc[0]), y=int(state_data["y"].iloc[0]))
            scoreboard.write(arg=f"{state}", align="center", font=("Courier", 10, "normal"), move=False)

data = {
    "state": states_to_learn,
    "x": x,
    "y": y,
}
df = pandas.DataFrame(data)
df.to_csv("state_to_learn.csv", index=False)

screen.exitonclick()
