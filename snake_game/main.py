from turtle import Screen
import time
from snake import Snake 
from food import Food
from scoreboard import Score

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)  # Stops the default animation

# Create game objects
snake = Snake()
food = Food()
score = Score()

# Keyboard controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start the game loop
game_is_on = True
while game_is_on:
    screen.update()  # Refresh the screen
    time.sleep(0.1)  # Control snake speed

    snake.move()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        score.score_update()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
        game_is_on = False

    # Detect collision with tail
    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            score.reset()
            snake.reset()
            game_is_on = False

screen.exitonclick()
