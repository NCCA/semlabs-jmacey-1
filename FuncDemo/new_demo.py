#!/usr/bin/env -S uv run --script

import random
import turtle


def move_to(current_turtle, x_pos, y_pos):
    """
    Move current turtle to position x,y with the pen up then put down
    """
    current_turtle.penup()
    current_turtle.goto(x_pos, y_pos)
    current_turtle.pendown()


def square(current_turtle, x_pos, y_pos, length):
    move_to(current_turtle, x_pos, y_pos)
    for _ in range(4):
        current_turtle.forward(length)
        current_turtle.right(90)


def triange(current_turtle, x_pos, y_pos, length):
    move_to(current_turtle, x_pos, y_pos)
    for _ in range(3):
        current_turtle.right(120)
        current_turtle.forward(length)


def get_random_pos_length():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    length = random.randint(10, 100)
    return x, y, length


my_turtle = turtle.Turtle()
my_turtle.speed(10)

# for SHAPE in ["s", "t", "t", "s"] * 100:
while True:
    SHAPE = random.choice(["s", "t"])
    if SHAPE == "square" or SHAPE == "s":
        x, y, length = get_random_pos_length()
        square(my_turtle, x, y, length)
    elif SHAPE == "triangle" or SHAPE == "t":
        x, y, length = get_random_pos_length()
        triange(my_turtle, x, y, length)
    else:
        print("shape not known")


turtle.done()
