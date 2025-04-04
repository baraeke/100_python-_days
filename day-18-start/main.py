# from turtle import Turtle, Screen 
# import random
# import tkinter

# # sam = Turtle()
# # # sam.shape("square")
# # sam.color("blue")
# # for _ in range(4):
# #     sam.forward(100)
# #     sam.right(90)


# # for _ in range(15):
# #     if _ % 2 != 0:
# #         sam.pendown()
# #         sam.forward(10)
# #         sam.penup()
# #     elif _ % 2 == 0:
# #         sam.forward(10)
# #         sam.pendown()
# #         sam.forward(10)

# # kelvin = Turtle()
# # color = ["red", "blue", "yellow", "green", "purple", "orange", "pink", "brown", "cyan"]
# # number_of_sides = 3

# # while number_of_sides <= 10:
# #     kelvin.home()
# #     choosen_color = random.choices(color)
# #     kelvin.color(choosen_color)
# #     angle = 360 / number_of_sides

# #     i = 0
# #     while i <= number_of_sides:
# #         kelvin.forward(100)
# #         kelvin.right(angle)
# #         i += 1

# #     number_of_sides += 1
# #     if number_of_sides < 3:
# #         break


# # dave = Turtle()
# # color = ["red", "blue", "yellow", "green", "purple", "orange", "pink", "brown", "cyan"]

# # def north():
# #     dave.color(random.choice(color))
# #     dave.forward(50)

# # def east():
# #     dave.color(random.choice(color))
# #     dave.right(90)
# #     dave.forward(50)

# # def south():
# #     dave.color(random.choice(color))
# #     dave.right(180)
# #     dave.forward(50)

# # def west():
# #     dave.color(random.choice(color))
# #     dave.right(270)
# #     dave.forward(50)

# # direction = {
# #     "north": north,
# #     "east": east,
# #     "south": south,
# #     "west": west,
# # }

# # number_of_times = 100
# # dave.width(10)
# # dave.speed(8)
# # while number_of_times > 0:
# #     random.choice(list(direction.values()))()
# #     number_of_times -= 1

# screen = Screen()
# screen.exitonclick() 

from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

def choosen_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)  
    random_color = (r, g, b)
    return random_color

def draw_circle():
    ebi.pencolor(choosen_color())
    ebi.speed("fastest")
    ebi.circle(100)

ebi = Turtle()
ebi.pensize(2)


number_of_times = 40
while number_of_times > 0:
    draw_circle()
    ebi.right(10)  # ✅ Rotates the turtle after each circle
    number_of_times -= 1

screen.exitonclick()
