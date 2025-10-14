#!/usr/bin/env -S uv run --script


import math
import random
import turtle


def move_to(current_turtle: "turtle.Turtle", x_pos: int, y_pos: int) -> None:
    """
    Move current turtle to position x,y with the pen up then put down
    """
    current_turtle.penup()
    current_turtle.goto(x_pos, y_pos)
    current_turtle.pendown()


def square(current_turtle, x_pos, y_pos, length) -> None:
    move_to(current_turtle, x_pos, y_pos)
    for _ in range(4):
        current_turtle.forward(length)
        current_turtle.right(90)


def triangle(current_turtle, x_pos, y_pos, length):
    move_to(current_turtle, x_pos, y_pos)
    for _ in range(3):
        current_turtle.right(120)
        current_turtle.forward(length)


def get_random_pos_length(x_extent: int = 400, y_extent: int = 400, max_length: int = 100) -> tuple[int, int, int]:
    """
    Get a random pos and length given input extents for x and y and length.
    Args:
        x_extent (int) the +/- extents from 0 in the x direction.
        y_extent (int) the +/- extents from 0 in the y direction.
        length (int) the 1- max_length random value.

    Returns:
        Tuple[int, int, int]: A tuple containing the x, y, and length values.

    """
    x = random.randint(-x_extent, x_extent)
    y = random.randint(-y_extent, y_extent)
    length = random.randint(1, max_length)
    return x, y, length


def unique_colour(inc: int = 25) -> tuple[int, int, int]:
    red = 0
    green = 0
    blue = 0
    while True:
        colour = (red, green, blue)
        red += inc
        if red >= 255:
            red = 0
            green += inc
        if green >= 255:
            green = 0
            blue += inc
        if blue >= 255:
            blue = 0
            red = 0
            green = 0
        yield colour


drawing_functions = [square, triangle]

tl = turtle.Turtle()
tl.speed(0)
turtle.colormode(255)
colour = unique_colour()
for _ in range(2000):
    r, g, b = next(colour)
    tl.pencolor(r, g, b)
    tl.fillcolor(r, g, b)
    x, y, length = get_random_pos_length(500, 500, 200)
    tl.begin_fill()
    random.choice(drawing_functions)(tl, x, y, length)
    tl.end_fill()
turtle.done()


# my_turtle = turtle.Turtle()
# my_turtle.pensize(20)
# running = True
# while running:
#     SHAPE = input("enter square or triangle> ")

#     if SHAPE == "square" or SHAPE == "s":
#         x, y, length = get_random_pos_length()
#         square(my_turtle, x, y, length)
#     elif SHAPE == "triangle" or SHAPE == "t":
#         x, y, length = get_random_pos_length()
#         triange(my_turtle, x, y, length)
#     elif SHAPE == "end":
#         running = False
#     else:
#         print("shape not known")


# # turtle.done()
