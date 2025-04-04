import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setup the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create player, scoreboard, and car list
player = Player()
scoreboard = Scoreboard()
cars = []  # Stores all active car objects

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Randomly create new cars
    if random.randint(1, 6) == 1:  # Adjust car spawn rate
        new_car = CarManager()
        cars.append(new_car)

    # Move all cars and remove those that leave the screen
    for car in cars[:]:
        car.move()
        if car.is_off_screen():
            car.hideturtle()  
            car.clear() 
            cars.remove(car)  

    # Check if player reaches the top
    if player.ycor() >= 280:
        scoreboard.score_update()  
        player.reset_player() 

    # Check for collisions with cars using bounding box detection
    for car in cars:
        player_left = player.xcor() - 10
        player_right = player.xcor() + 10
        player_top = player.ycor() + 10
        player_bottom = player.ycor() - 10

        car_left = car.xcor() - 30
        car_right = car.xcor() + 30
        car_top = car.ycor() + 10
        car_bottom = car.ycor() - 10

        # Check if the bounding boxes overlap
        if (player_right > car_left and player_left < car_right and 
            player_top > car_bottom and player_bottom < car_top):
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
