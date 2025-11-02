# -----------------------------------------
# U.S. States Guessing Game
# -----------------------------------------
# This educational Python game challenges players
# to name all 50 U.S. states.
# It uses a turtle graphics map and pandas for data handling.
# The player's guesses are written on the map, and
# unguessed states are saved to a CSV file for learning later.
# -----------------------------------------

import turtle
import pandas

# -----------------------------
# SETUP: Screen and Background
# -----------------------------
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load and display the U.S. blank map image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create a turtle object for writing state names on the map
t = turtle.Turtle()
t.hideturtle()     # Hide the turtle cursor for a cleaner UI
t.penup()          # Lift the pen to move without drawing lines

# -----------------------------
# LOAD DATA USING PANDAS
# -----------------------------
# The CSV file contains columns: state, x, y
# where x and y represent coordinates on the map image.
data = pandas.read_csv("50_states.csv")

# Convert the "state" column into a list for easy lookup
all_states = data.state.to_list()

# Keep track of correctly guessed states
guessed_states = []

# -----------------------------
# MAIN GAME LOOP
# -----------------------------
while len(guessed_states) < 50:
    # Prompt the user for a state name, showing progress in the title
    answer_text = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    ).title()  # Capitalize the first letter for consistency with data

    # -----------------------------
    # EXIT CONDITION
    # -----------------------------
    if answer_text == "Exit":
        # Create a list of states not yet guessed
        missing_states = [state for state in all_states if state not in guessed_states]
        # Save missing states to a CSV file for learning later
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # -----------------------------
    # CORRECT GUESS LOGIC
    # -----------------------------
    if answer_text in all_states and answer_text not in guessed_states:
        guessed_states.append(answer_text)
        # Get the row of data for the guessed state
        state_data = data[data.state == answer_text]
        # Move the turtle to the correct map coordinates
        t.goto(state_data.x.item(), state_data.y.item())
        # Write the state's name on the map
        t.write(answer_text)

# -----------------------------
# END OF GAME
# -----------------------------
# If the user exits or completes all 50 states,
# the program saves the list of missing states and ends.
