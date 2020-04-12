"""
This modle contains the example_05 class api
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


class Rectangle:
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
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self.pen_color = pen_color
        self.fill_color = fill_color

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
        return self._width * self._height

    def set_pen_color(self, color: str) -> Rectangle:
        """Set the pen color of the rectangle
        
        Arguments:
            color {str} -- the color name to set the rectangle pen to
        
        Returns:
            Rectangle -- returns self for chaining
        """
        self.pen_color = color
        return self

    def set_fill_color(self, color: str) -> Rectangle:
        """Set the fill color of the rectangle
        
        Arguments:
            color {str} -- the color name to set the rectangle fill to
        
        Returns:
            Rectangle -- returns self for chaining
        """
        self.fill_color = color
        return self


rectangle = Rectangle(10, 10, 10, 20)
print(f"The rectangle area = {rectangle.area()}")

rectangle.x += 15
rectangle.y += 15
rectangle.set_pen_color("BLUE").set_fill_color("GREEN")
print(
    f"{rectangle.pen_color} rectangle filed with {rectangle.fill_color}, position x={rectangle.x}, y={rectangle.y}"
)