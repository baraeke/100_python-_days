from turtle import Turtle

WIDTH = 1
HEIGHT = 5
MOVE_DISTANCE = 20
TOP_EDGE = 250
BOTTOM_EDGE = -250

class Paddle(Turtle):
    def __init__(self, xcor=350, ycor=0):
        super().__init__()
        self.create_turtle(xcor, ycor)

    def create_turtle(self, xcor, ycor):
        self.shape("square")
        self.color("orange")
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.penup()
        self.goto(x=xcor, y=ycor)

    def move_up(self):
        # Move up if not at the top edge
        if self.ycor() < TOP_EDGE:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def move_down(self):
        # Move down if not at the bottom edge
        if self.ycor() > BOTTOM_EDGE:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
