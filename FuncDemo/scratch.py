#!/usr/bin/env -S uv run --script


def counter():
    a = 0
    while True:
        a += 1
        if a > 1000:
            break
        yield a


my_counter = counter()
for a in my_counter:
    print(a)
