import turtle
from turtle import Turtle, Screen
import random


# ronaldo = Turtle()
# ronaldo.shape("turtle")
# ronaldo.color("red")

# Challenge 1
# for x in range(4):
#   ronaldo.forward(100)
#   ronaldo.right(90)

# Challenge 2
# cristiano_ronaldo = Turtle()

# for _ in range(15):
#   cristiano_ronaldo.forward(10)
#   cristiano_ronaldo.penup()
#   cristiano_ronaldo.forward(10)
#   cristiano_ronaldo.pendown()

# Challenge 3
def make_shape(sides):
    ronaldo = Turtle()

    def change_color():
        R = random.random()
        B = random.random()
        G = random.random()

        ronaldo.color(R, G, B)

    def angle():
        return 360 / int(sides)

    change_color()
    for _ in range(sides):
        ronaldo.forward(100)
        ronaldo.right(angle())



times = 3
for _ in range(8):
    make_shape(times)
    times += 1

screen = Screen()
screen.exitonclick()
