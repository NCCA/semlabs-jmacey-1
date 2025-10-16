from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class rgba:
    r: int = 0
    g: int = 0
    b: int = 0
    a: int = 255

    def get_tuple(self) -> Tuple[int, int, int, int]:
        return (self.r, self.g, self.b, self.a)

    def __post_init__(self):
        for component in ("r", "g", "b", "a"):
            value = getattr(self, component)
            if not isinstance(value, int) or not 0 <= value <= 255:
                raise ValueError(f"RGBA component {component} must be int between 0-255")


class Image:
    def __init__(self, width: int = 0, height: int = 0) -> None:
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
