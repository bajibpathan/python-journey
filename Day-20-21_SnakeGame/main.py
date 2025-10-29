# Import necessary modules and classes
from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time

# Setup game screen dimensions and appearance
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off automatic screen updates to manually control rendering

# Create instances of Snake, Food, and Scoreboard classes
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Listen for keyboard input to control snake direction
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game state flag
game_is_on = True

# Main game loop
while game_is_on:
    screen.update()      # Manually update the screen to show latest snake position
    time.sleep(0.1)      # Controls snake speed
    snake.move()         # Move the snake one step forward

    # --- Collision with Food ---
    if snake.head.distance(food) < 15:   # Check if snake is close enough to eat food
        food.refresh()                   # Move food to a new random position
        snake.extend()                   # Add new segment to the snake
        scoreboard.increase_score()      # Increase and update the score

    # --- Collision with Wall ---
    if (
        snake.head.xcor() > 280 or snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()           # Display "GAME OVER" when snake hits wall

    # --- Collision with Tail ---
    for segment in snake.segments[1:]:   # Check collision with body (ignore head)
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Keeps window open until user clicks on it
screen.exitonclick()
