from turtle import Turtle
import random

class Food(Turtle):
    """Creates and manages the food object for the snake to eat."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Smaller food size
        self.color("blue")
        self.speed("fastest")
        self.refresh()  # Place food at random location on creation

    def refresh(self):
        """Move the food to a new random location."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
