from turtle import Turtle
import random

# Constants for car behavior and speed
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """Handles car creation, movement, and speed management."""

    def __init__(self):
        self.all_cars = []             # List to store all cars on screen
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Create a new car at random intervals and random Y positions."""
        random_chance = random.randint(1, 6)
        # Create a car only occasionally to avoid overcrowding
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)   # Start from the right edge
            self.all_cars.append(new_car)

    def move_cars(self):
        """Move all cars leftward across the screen."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increase car movement speed after each successful crossing."""
        self.car_speed += MOVE_INCREMENT
