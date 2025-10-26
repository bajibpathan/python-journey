# hirst_painting.py
# ---------------------------------------------------
# Hirst Painting Project using the Turtle Graphics module.
# This program creates a colorful grid of dots inspired by
# Damien Hirst's spot paintings.
# ---------------------------------------------------

import turtle as turtle_module
import random

# Set the turtle color mode to use RGB values instead of color names
turtle_module.colormode(255)

# Create the turtle instance for drawing
tim = turtle_module.Turtle()
tim.speed("fastest")      # Set the drawing speed to the fastest
tim.penup()               # Lift the pen to avoid drawing lines while moving
tim.hideturtle()          # Hide the turtle cursor for a cleaner output

# A pre-defined list of RGB color tuples extracted from an image using colorgram
color_list = [
    (202, 164, 110), (240, 245, 241), (236, 239, 243),
    (149, 75, 50), (222, 201, 136), (53, 93, 123),
    (170, 154, 41), (138, 31, 20), (134, 163, 184),
    (197, 92, 73), (47, 121, 86), (73, 43, 35),
    (145, 178, 149), (14, 98, 70), (232, 176, 165),
    (160, 142, 158), (54, 45, 50), (101, 75, 77),
    (183, 205, 171), (36, 60, 74), (19, 86, 89),
    (82, 148, 129), (147, 17, 19), (27, 68, 102),
    (12, 70, 64), (107, 127, 153), (176, 192, 208),
    (168, 99, 102)
]

# Position the turtle to the starting point (bottom-left corner of the canvas)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# Define the total number of dots to draw
number_of_dots = 100

# Loop through the number of dots to create a 10x10 grid
for dot_count in range(1, number_of_dots + 1):
    # Draw a dot with a random color from the color list
    tim.dot(20, random.choice(color_list))
    # Move forward to position the next dot
    tim.forward(50)

    # After every 10 dots, move up to start a new row
    if dot_count % 10 == 0:
        tim.setheading(90)   # Turn upwards
        tim.forward(50)      # Move to the next row
        tim.setheading(180)  # Turn left
        tim.forward(500)     # Go back to the start of the row
        tim.setheading(0)    # Reset direction to the right

# Keep the window open until the user clicks
screen = turtle_module.Screen()
screen.exitonclick()
