"""
This modle contains the example_04 class api
construction
"""

from __future__ import annotations
from typing import Tuple
from typing import Type


class Rectangle:
    """This class defines a simple rectangle object
    """
    def __init__(self, x: int, y: int, width: int, height: int, pen_color: str = "BLACK"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pen_color = pen_color

    def area(self) -> int:
        """Calculate and return the area of the rectangle
        
        Returns:
            int -- the width * height area
        """
        return self.width * self.height

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
print(rectangle.area())

rectangle.x += 15
rectangle.y += 15
rectangle.set_pen_color("BLUE").set_fill_color("GREEN")
print(f"{rectangle.pen_color} rectangle filed with {rectangle.fill_color} after move, x={rectangle.x}, y={rectangle.y}")
