#!/usr/bin/env -S uv run --script
#
class Colour:
    def __init__(self, r=0, g=0, b=0, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @classmethod
    def from_list(cls, values):
        colour = cls()
        colour.r = values[0]
        colour.g = values[1]
        colour.b = values[2]
        colour.a = values[3]
        return colour

    def __str__(self):
        return f"[{self.r},{self.g},{self.b},{self.a}]"


red = Colour(255, 0, 0, 255)
print(red)
black = Colour()
print(black)
white = Colour.from_list((255,255,255,255))
print(white)
white.r = 99
print(white)
