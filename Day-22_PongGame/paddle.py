from turtle import Turtle

class Paddle(Turtle):
    """Represents a player paddle in the Pong game."""

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # Elongate paddle vertically
        self.penup()
        self.goto(position)                            # Move paddle to initial position

    def go_up(self):
        """Move paddle upward by 20 pixels."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Move paddle downward by 20 pixels."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
