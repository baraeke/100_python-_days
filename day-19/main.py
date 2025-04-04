# from turtle import Turtle, Screen

# # Create the turtle and screen
# sam = Turtle()
# screen = Screen()

# # Move forward by 20 units
# def move():
#     sam.forward(20)

# # Turn left by 90 degrees
# def up():
#     sam.left(90)

# # Turn right by 90 degrees
# def down():
#     sam.right(90)

# # Turn left by 90 degrees (same as up, but you can customize if needed)
# def left():
#     sam.left(90)

# # Turn right by 90 degrees (same as down, but you can customize if needed)
# def right():
#     sam.right(90)

# # Listen for key presses
# screen.listen()

# # Bind keys to the functions
# screen.onkey(key="space", fun=move)
# screen.onkey(key="Up", fun=up)
# screen.onkey(key="Down", fun=down)
# screen.onkey(key="Left", fun=left)
# screen.onkey(key="Right", fun=right)

# # Exit on click
# screen.exitonclick()

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width= 500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter  a color: ")
colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Black"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
game_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    game_on = True

while game_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle.lower() == user_bet.lower():
                print(f"You have won! The {winning_turtle} turle is the winner!")
                game_on = False
            else:
                print(f"You have Lost! The {winning_turtle} turle is the winner!")
                game_on = False
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()