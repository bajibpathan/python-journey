from turtle import Turtle

class Ball(Turtle):
    """Controls the Pong ball — movement, bouncing, and reset behavior."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10     # Movement increment in X direction
        self.y_move = 10     # Movement increment in Y direction
        self.move_speed = 0.1  # Speed of the ball (lower = faster)

    def move(self):
        """Move the ball by updating its (x, y) position."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse the ball's Y direction when hitting top/bottom walls."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse X direction when hitting paddles and increase speed."""
        self.x_move *= -1
        self.move_speed *= 0.9   # Speed up slightly after every paddle hit

    def reset_position(self):
        """Reset the ball to the center after a point and reverse direction."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
