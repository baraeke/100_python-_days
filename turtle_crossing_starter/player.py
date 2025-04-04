from turtle import Turtle, Screen, register_shape

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.color("blue")
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        """Move the car up by MOVE_DISTANCE each time it's called"""
        if self.ycor() < FINISH_LINE_Y:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reset_player(self):
        """Resets the player's position back to the starting point."""
        self.goto(STARTING_POSITION)