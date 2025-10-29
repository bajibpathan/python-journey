from turtle import Turtle

# Initial snake body positions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# Directions (in degrees)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Manages the snake’s body, movement, and direction."""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # Reference to the snake's head segment

    def create_snake(self):
        """Create initial snake body with 3 segments."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a single segment at the given position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()  # Prevents line drawing between movements
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extend the snake by one segment."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward by shifting each segment to the position of the one in front."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # --- Direction Controls ---
    def up(self):
        """Change direction to up (if not currently moving down)."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change direction to down (if not currently moving up)."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change direction to left (if not currently moving right)."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change direction to right (if not currently moving left)."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
