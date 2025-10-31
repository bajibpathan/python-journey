from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

# ----------------------------------------
# Main Game Setup
# ----------------------------------------

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic animation for smoother movement

# Create player, car manager, and scoreboard objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for user input (Up arrow key)
screen.listen()
screen.onkey(player.go_up, "Up")

# ----------------------------------------
# Game Loop
# ----------------------------------------
game_is_on = True

while game_is_on:
    time.sleep(0.1)        # Control game speed
    screen.update()         # Update the screen after all movements

    # Generate and move cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision between player and any car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect if player successfully crosses the road
    if player.is_at_finish_line():
        player.go_to_start()         # Move player back to starting position
        car_manager.level_up()       # Increase car speed for next level
        scoreboard.increase_level()  # Update the level display

# Exit game on click
screen.exitonclick()
