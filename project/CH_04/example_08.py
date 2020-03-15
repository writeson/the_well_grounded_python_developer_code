"""
This modle contains the example_08 class api
construction
"""

from __future__ import annotations
from typing import Tuple
from typing import Type
from dataclasses import dataclass


@dataclass
class Screen:
    """This assumes the screen origin is 0, 0
    """

    max_x: int = 1024
    max_y: int = 1024


class Color:
    COLORS = ["RED", "GREEN", "BLUE", "YELLOW", "ORANGE", "WHITE", "BLACK"]

    def __init__(self, color: str):
        if color in Color.COLORS:
            self._color = color
        else:
            self._color_error(color)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if value in Color.COLORS:
            self._color = Color
        else:
            self._color_error(color)

    def _color_error(self, color):
        raise AttributeError("Invalid color", color)


class Shape:
    """This class provides the functionality common to all
    shapes
    """

    def __init__(
        self, x: int, y: int, pen_color: str = "BLACK", fill_color: str = "BLUE"
    ):
        self._x = x
        self._y = y
        self.pen = Color(pen_color)
        self.fill = Color(fill_color)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: int):
        """Limit the self._x to within the screen dimensions
        
        Arguments:
            value {int} -- the value to set x to
        """
        if self._x + value < 0:
            self._x = 0
        elif self._x + value > Screen.max_x:
            self._x = Screen.max_x
        else:
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        """Limit the self._y to within the screen dimensions
        
        Arguments:
            value {int} -- the value to set y to
        """
        if self._y + value < 0:
            self._y = 0
        elif self._y + value > Screen.max_y:
            self._y = Screen.max_y
        else:
            self._y = value

    def set_pen_color(self, color: Color) -> Shape:
        """Set the pen color of the rectangle
        
        Arguments:
            color {str} -- the color name to set the rectangle pen to
        
        Returns:
            Rectangle -- returns self for chaining
        """
        self.pen = color
        return self

    def set_fill_color(self, color: Color) -> Shape:
        """Set the fill color of the rectangle
        
        Arguments:
            color {str} -- the color name to set the rectangle fill to
        
        Returns:
            Rectangle -- returns self for chaining
        """
        self.fill = color
        return self

    def move(self, x_delta: int, y_delta: int):
        """Method to move objects around without touch attributes directly
        
        Arguments:
            x_delta {int} -- the amount to move on the x-axis
            y_delta {int} -- the amount to move on the y-axis
        """
        self.x += x_delta
        self.y += y_delta


class Rectangle(Shape):
    """This class defines a simple rectangle object
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        pen_color: str = "BLACK",
        fill_color: str = "BLUE",
    ):
        super().__init__(x, y, pen_color, fill_color)
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def area(self) -> int:
        """Calculate and return the area of the rectangle
        
        Returns:
            int -- the width * height volume
        """
        return self.width * self.height


class Square(Rectangle):
    """This class defines a simple square object
    """

    def __init__(
        self,
        x: int,
        y: int,
        size: int,
        pen_color: str = "BLACK",
        fill_color: str = "BLUE",
    ):
        super().__init__(x, y, size, size, pen_color, fill_color)

    @property
    def size(self):
        return self._width

    def move(self, x_delta: int, y_delta: int):
        """This method moves square instance by delta * 2
        
        Arguments:
            x_delta {int} -- the amount to move on the x-axis
            y_delta {int} -- the amount to move on the y-axis
        """
        super().move(x_delta * 2, y_delta * 2)


shapes = [
    Rectangle(10, 10, 10, 20, "GREEN", "YELLOW"),
    Square(25, 10, 10, "RED", "BLUE"),
]

# identify the shapes
for shape in shapes:ß
    print(
        f"shape is a {type(shape).__name__}, and is an instance of Shape: {isinstance(shape, Shape)}"
    )
    print(
        f"{type(shape).__name__} pen color: {shape.pen.color} and filled with {shape.fill.color}"
    )
    print(f"{type(shape).__name__} area = {shape.area()}")

print()

# move the shapes diagonally down the screen
for move_increment in [10] * 5:
    for shape in shapes:
        shape.move(move_increment, move_increment)
        print(f"{type(shape).__name__} position x={shape.x}, y={shape.y}")

