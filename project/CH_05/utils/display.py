# Boilerplate display window functionality

import arcade

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
RADIUS = 150

# Classes
class Display(arcade.Window):
    """Main display window
    """

    def __init__(self, screen_title):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, screen_title)

        # Set the background window
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """Called whenever you need to draw your window
        """

        # Clear the screen and start drawing
        arcade.start_render()

        # Draw a blue circle
        arcade.draw_circle_filled(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLUE
        )
