import sys


class NumberStats:
    def __init__(self):
        self.min = sys.maxsize
        self.max = -sys.maxsize - 1
        self.num_items = 0
        self.running_total = 0

    def add_number(self, value):
        self.running_total += value
        self.num_items += 1
        self._update_min_max(value)

    def _update_min_max(self, value):
        if value >= self.max:
            self.max = value
        if value <= self.min:
            self.min = value

    def average(self):
        return self.running_total / self.num_items

    def __str__(self):
        return f"{self.min=} {self.max=} {self.num_items=} {self.running_total=}"

    def __repr__(self):
        return f"NumberStats{self.min=} {self.max=} {self.num_items=} {self.running_total=}"
