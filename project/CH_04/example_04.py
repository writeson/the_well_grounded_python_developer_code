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
    def __init__(self, x: int, y: int, width: int, height: int, color: str = "BLACK"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def volume(self) -> int:
        """Calculate and return the volume of the rectangle
        
        Returns:
            int -- the width * height volume
        """
        return self.width * self.height

    def move(self, delta_x: int = 0, delta_y: int = 0) -> Rectangle:
        """Move the rectangle by the amount indicated by
        the delta_x and delta_y values
        
        Keyword Arguments:
            delta_x {int} -- move amount on the x axis
            delta_y {int} -- move amount on the y axis
        
        Returns:
            Rectangle -- returns self for chaining
        """
        self.x += delta_x
        self.y += delta_y
        return self

    def setcolor(self, color: str) -> Rectangle:
        """Set the color of the rectangle
        
        Arguments:
            color {str} -- the color name to set the rectangle to
        
        Returns:
            Rectangle -- returns self for chaining
        """     
        self.color = color

rectangle = Rectangle(10, 10, 10, 20)
print(rectangle.volume())

rectangle.move(15, 15).setcolor("BLUE")
print(f"{rectangle.color} rectangle after move, x={rectangle.x}, y={rectangle.y}")
