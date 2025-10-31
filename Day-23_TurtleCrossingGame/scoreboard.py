from turtle import Turtle

# Constants for player movement and level goals
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Represents the player's turtle trying to cross the road."""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)  # Point turtle upwards

    def go_up(self):
        """Move the turtle forward (up) each time Up arrow is pressed."""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Return the turtle to the starting position."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Check if the player has reached the finish line."""
        return self.ycor() > FINISH_LINE_Y
