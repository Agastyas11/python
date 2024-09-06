from turtle import Turtle, Screen

ronaldo = Turtle()
screen = Screen()


def move_forwards():
    ronaldo.forward(10)


def turn_left():
    ronaldo.tilt(10)


def move_backwards():
    ronaldo.back(10)


def turn_right():
    ronaldo.right(10)


def recenter():
    ronaldo.clear()
    ronaldo.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=recenter)

screen.exitonclick()
