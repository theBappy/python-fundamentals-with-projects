from turtle import *
import turtle as t
import random
import time

tommy = t.Turtle()

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b

def turtle_movement():
    tommy.pensize(10)
    rgb = random_color()
    direction = random.randint(1, 4)
    tommy.pencolor(rgb[0], rgb[1], rgb[2])

    if direction == 1:
        tommy.left(90)
        tommy.forward(30)
        time.sleep(0.5)
    elif direction == 2:
        tommy.right(90)
        tommy.forward(30)
        time.sleep(0.5)
    elif direction == 3:
        tommy.forward(30)
        time.sleep(0.5)
    elif direction == 4:
        tommy.backward(30)
        time.sleep(0.5)

colors = [
    "GreenYellow",
    "Tan", 
    "Chartreuse",
    "LightSkyBlue",
    "DeepPink", 
    "MediumSlateBlue"
]

t.pensize(10)

for _ in range(0, 200):
    turtle_movement()

screen = Screen()
screen.exitonclick()
