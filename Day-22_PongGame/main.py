import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# -----------------------------
# Main Game Setup
# -----------------------------

# Create the main game screen
screen = Screen()
screen.bgcolor("black")               # Set background color to black for a classic Pong look
screen.setup(width=800, height=600)   # Set the screen size
screen.title("Pong")                  # Set window title
screen.tracer(0)                      # Turn off automatic animation for smoother movement

# Create paddles for both players
r_paddle = Paddle((350, 0))           # Right paddle starting position
l_paddle = Paddle((-350, 0))          # Left paddle starting position

# Create ball and scoreboard objects
ball = Ball()
scoreboard = Scoreboard()

# -----------------------------
# Keyboard Controls
# -----------------------------
screen.listen()
# Right paddle controls
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# Left paddle controls
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# -----------------------------
# Main Game Loop
# -----------------------------
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)   # Control the game speed based on ball movement
    screen.update()               # Update the screen manually
    ball.move()                   # Move the ball forward each frame

    # Detect collision with top or bottom wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with either paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Exit on mouse click
screen.exitonclick()
