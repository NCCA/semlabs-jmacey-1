import pytest

from image import Image, rgba


@pytest.fixture
def red() -> rgba:
    return rgba(255, 0, 0)


def test_image_default():
    img = Image()
    assert img.width == 0
    assert img.height == 0
    assert not "start here "


def test_default_rgba():
    """
    A default rgba should have 0,0,0,255
    for r,g,b,a in that order
    """
    c = rgba()
    assert (c.r, c.g, c.b, c.a) == (0, 0, 0, 255)


def test_user_values():
    """
    test to see if I can build with rgb, and rgba values
    """
    c = rgba(255, 128, 0)
    assert (c.r, c.g, c.b, c.a) == (255, 128, 0, 255)
    c = rgba(255, 128, 0, 128)
    assert (c.r, c.g, c.b, c.a) == (255, 128, 0, 128)


def test_red(red):
    assert red.r == 255
    assert red.g == 0
    assert red.b == 0
    assert red.a == 255
    assert (red.r, red.g, red.b, red.a) == (255, 0, 0, 255)


def test_get_tuple(red):
    assert red.get_tuple() == (255, 0, 0, 255)


@pytest.mark.parametrize("comp, value", [("r", "-1"), ("g", 256), ("b", 1000), ("a", 1.2), ("r", "string")])
def test_out_of_range(comp, value):
    with pytest.raises(ValueError):
        kwargs = {comp: value}
        rgba(**kwargs)
