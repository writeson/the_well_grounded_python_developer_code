# Boilerplate display window functionality

from __future__ import annotations
import arcade
from random import choice

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800


class Rectangle:
    """This class defines a simple rectangle object
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        pen_color: tuple = arcade.color.BLACK,
        fill_color: tuple = (132, 132, 130),
        dir_x: int = 1,
        dir_y: int = 1,
        vel_x: int = 1,
        vel_y: int = 1
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pen_color = pen_color
        self.fill_color = fill_color
        self.dir_x = 1 if dir_x > 0 else -1
        self.dir_y = 1 if dir_y > 0 else -1
        self.vel_x = vel_x
        self.vel_y = vel_y

    def set_pen_color(self, color: tuple) -> Rectangle:
        """Set the pen color of the rectangle
        
        Arguments:
            color {tuple} -- the color tuple to set the rectangle pen to
        
        Returns:
            Rectangle -- returns self for chaining
        """
        self.pen_color = color
        return self

    def set_fill_color(self, color: tuple) -> Rectangle:
        """Set the fill color of the rectangle
        
        Arguments:
            color {tuple} -- the color tuple to set the rectangle fill to
        
        Returns:
            Rectangle -- returns self for chaining
        """
        self.fill_color = color
        return self

    def draw(self):
        """Draw the rectangle based on the current state
        """
        arcade.draw_xywh_rectangle_filled(
            self.x, self.y, self.width, self.height, self.fill_color
        )
        arcade.draw_xywh_rectangle_outline(
            self.x, self.y, self.width, self.height, self.pen_color, 3
        )


class Display(arcade.Window):
    """Main display window
    """

    def __init__(self, screen_title):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, screen_title)

        # Create the retangles collection
        self._rectangles = []

        # Set the background window
        arcade.set_background_color(arcade.color.WHITE)

    @property
    def rectangles(self):
        return self._rectangles

    def append(self, rectangle: Rectangle):
        """Appends an instance of a rectangle to the list of rectangles
        
        Arguments:
            rectangle {Rectangle} -- Rectangle instance to add to the list
        """
        self._rectangles.append(rectangle)

    def on_update(self, delta_time):
        """Update the position of the rectangles in the display
        """
        for rectangle in self._rectangles:
            rectangle.x += rectangle.vel_x
            rectangle.y += rectangle.vel_y

    def on_draw(self):
        """Called whenever you need to draw your window
        """

        # Clear the screen and start drawing
        arcade.start_render()

        # Draw the rectangles
        for rectangle in self._rectangles:
            rectangle.draw()


# Main code entry point
if __name__ == "__main__":
    # Create the display instance
    display = Display("Example 01")

    # Create a rectangle instance
    rectangle = Rectangle(20, 20, 100, 200)

    # Append the rectangle to the display rectangles list
    display.append(rectangle)

    # Run the application
    arcade.run()
