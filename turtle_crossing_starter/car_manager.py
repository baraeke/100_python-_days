from turtle import Turtle, register_shape
import random

# Car Shape 1: Compact Car
compact_car = [
    (-20, 10), (20, 10), (25, 5), (25, -5), (20, -10), (-20, -10), (-25, -5), (-25, 5)
]

# Car Shape 2: Truck
truck = [
    (-30, 15), (30, 15), (30, 5), (20, 5), (20, -15), (-20, -15), (-20, 5), (-30, 5)
]

# Car Shape 3: Sports Car
sports_car = [
    (-25, 8), (25, 8), (28, 3), (28, -3), (25, -8), (-25, -8), (-28, -3), (-28, 3)
]

# Car Shape 4: SUV
suv = [
    (-30, 12), (30, 12), (30, -10), (20, -15), (-20, -15), (-30, -10)
]

# Register the shapes
register_shape("compact_car", tuple(compact_car))
register_shape("truck", tuple(truck))
register_shape("sports_car", tuple(sports_car))
register_shape("suv", tuple(suv))

cars = ["compact_car", "truck", "sports_car", "suv"]

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RIGHT_EDGE_X = 270 
LEFT_EDGE_X = -320
Y_POSITIONS = [-200, -100, 0, 100, 200]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(random.choice(cars))
        self.color(random.choice(COLORS))
        self.penup()
        self.y_cor = random.choice(Y_POSITIONS)
        self.goto(RIGHT_EDGE_X, self.y_cor)

    def move(self):
        """Moves the car left continuously"""
        self.goto(self.xcor() - MOVE_INCREMENT, self.y_cor)

    def is_off_screen(self):
        """Returns True if the car is off the screen"""
        return self.xcor() < LEFT_EDGE_X
