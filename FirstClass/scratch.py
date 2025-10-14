#!/usr/bin/env -S uv run --script
#


class DummyClass:
    def __init__(self):
        self.x = 0

    def setup(self):
        self.value = 99


a = DummyClass()
a.setup()
a.x = 99
print(dir(a))
b = DummyClass()
print(dir(b))
