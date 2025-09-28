
# Reeborg's World Maze Solver
# This program solves the Reeborg's World Maze puzzle using the right-hand rule algorithm.

# Define a helper function to turn right, since only turn_left() is available in Reeborg's World
def turn_right():
    for iteration in range(3):
        turn_left()

# Move forward until you hit a wall, then turn left to start following the maze
while front_is_clear():
    move()
turn_left()

# Main loop to solve the maze until the goal is reached
while not at_goal():
    # If the path to the right is clear, take it (right-hand rule for maze solving)
    if right_is_clear():
        turn_right()
        move()
    # If the path ahead is clear, move forward
    elif front_is_clear():
        move()
    # If neither right nor forward is available, turn left to keep searching
    else:
        turn_left()
