#!/usr/bin/env -S uv run --script

# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///


class NumberValue:
    def __init__(self, value):
        self.value = value

    def square(self):
        self.value = self.value * self.value

    def debug(self):
        print(f"{self.value=}")


a = NumberValue(10)
b = NumberValue(22)
a.debug()
for _ in range(10) :
    a.square()
a.debug()
b.debug()


"""
We need to keep a running total of values added to the System. We should be able to find the average min and max values

"""


# def add(a, b):
#     return a + b


# def sub(a, b):
#     return a - b


# v1 = 3
# v2 = 6

# result = add(v1, v2)
# result = sub(result, v2)
# print(result)
