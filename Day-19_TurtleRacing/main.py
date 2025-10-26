# Importing necessary modules
# 'Turtle' and 'Screen' are from the turtle graphics library for visual simulation.
# 'random' is used to generate random movement for each turtle.
from turtle import Turtle, Screen
import random

# This flag controls when the race starts and stops.
is_race_on = False

# Setting up the race window
screen = Screen()
screen.setup(width=500, height=400)  # Sets window size

# Asking the user to place a bet by choosing a turtle color
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
)

# Defining colors for the six turtles and their vertical positions
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# A list to hold all turtle racers
all_turtles = []

# Creating six turtles, giving each one a unique color and position
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")              # Create a turtle with turtle shape
    new_turtle.color(colors[turtle_index])           # Assign color from the list
    new_turtle.penup()                               # Lift pen to avoid drawing lines while positioning
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # Position turtle at starting line
    all_turtles.append(new_turtle)                   # Add to the list of turtles

# Start the race only if the user placed a bet
if user_bet:
    is_race_on = True

# Main race loop
while is_race_on:
    for turtle in all_turtles:
        # Check if any turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            # Display race result based on the user's bet
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner! 🎉")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner! 🏁")

        # Move each turtle forward by a random distance (simulating unpredictable race)
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Keeps the screen open until user clicks on it
screen.exitonclick()
