from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

TOP_EDGE = 285
BOTTOM_EDGE = -285
LEFT_EDGE = -385
RIGHT_EDGE = 385

# Screen setup
screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Paddle setup
r_paddle = Paddle()
l_paddle = Paddle(xcor=-350, ycor=0)
l_paddle.color("green")

# Ball setup
ball = Ball()

# Scoreboard setup
scoreboard = Scoreboard()

# r_paddle keyboard controls
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

# l_paddle keyboard controls
screen.onkeypress(l_paddle.move_up, "q")
screen.onkeypress(l_paddle.move_down, "z")

# Enable tracer after setup
screen.tracer(1)

# Game loop
speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move_ball()

    # Check for bounce at top or bottom
    if ball.ycor() >= TOP_EDGE or ball.ycor() <= BOTTOM_EDGE:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 328 or ball.distance(l_paddle) < 50 and ball.xcor() < -328:
        ball.bounce_x()
        speed *= 0.9

    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_score()
        # to_replay = screen.textinput(title="Play Again?", prompt="Player L, do you want to play again? (yes/no)").lower()
        # if to_replay == "no":
        #     game_is_on = False
        #     scoreboard.game_over()
        # elif to_replay == "yes":
        #     ball.goto(x=0, y=0)
        #     scoreboard.update_score()

    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_score()
        # scoreboard.r_player_score += 1
        # to_replay = screen.textinput(title="Play Again?", prompt="Player R, do you want to play again? (yes/no)").lower()
        # if to_replay == "no":
        #     game_is_on = False
        #     scoreboard.game_over()
        # elif to_replay == "yes":
        #     ball.goto(x=0, y=0)
        #     scoreboard.update_score()

screen.exitonclick()