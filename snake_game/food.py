from turtle import Turtle
import random

class Food(Turtle):
    """Represents the food in the game."""

    def __init__(self):
        """Initializes the food and places it randomly on the screen."""
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make food smaller
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Moves the food to a new random location on the screen."""
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)
