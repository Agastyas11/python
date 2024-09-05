# Rule 1: 10 by 10 rows of spots
# Rule 2: Each dot should be 20 in size and spaced about 50 paces.
from turtle import Turtle, Screen
import random


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    return (R, G, B)


ronaldo = Turtle()


def next_line():
    ronaldo.penup()
    ronaldo.left(90)
    ronaldo.forward(50)
    ronaldo.left(90)
    ronaldo.forward(500)
    ronaldo.right(180)


for _ in range(10):
    for _ in range(10):
        new_color = change_color()
        ronaldo.dot(20, new_color)
        ronaldo.penup()
        ronaldo.forward(50)
    next_line()

screen = Screen()
screen.exitonclick()
