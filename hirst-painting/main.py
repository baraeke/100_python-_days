from turtle import Turtle, Screen
import random


screen = Screen()
screen.colormode(255)
screen.setworldcoordinates(-100, -100, 100, 100)



sam = Turtle()
# # import colorgram

# number_of_colors = 30
# extract = colorgram.extract('color.jpeg', number_of_colors)
# colors = []

# for color_object in extract:
#     rgb = color_object.rgb
#     color_tuple = (rgb.r, rgb.g, rgb.b) 
#     colors.append(color_tuple)


colors = [
    (235, 226, 87), (210, 161, 109), (113, 177, 212), (201, 5, 68),
    (230, 52, 128), (196, 77, 19), (217, 133, 177), (193, 164, 15),
    (34, 106, 166), (11, 21, 62), (32, 189, 114), (232, 224, 4),
    (18, 28, 171), (122, 188, 161), (204, 32, 127), (233, 165, 197),
    (14, 183, 211), (10, 45, 24), (38, 132, 72), (45, 15, 10),
    (105, 92, 210), (139, 219, 203), (185, 13, 6), (135, 218, 232),
    (229, 73, 45), (169, 180, 229)
]

def select_color():
    return random.choice(colors)


def print_and_move():
    sam.dot(20, select_color())
    sam.penup()
    sam.forward(10)
    sam.pendown()

sam.speed("fastest")
# sam.penup()
sam.goto(-100,-100)


condition = 21
while condition > 0:
    print_and_move()
    

    condition -= 1

screen.exitonclick()


