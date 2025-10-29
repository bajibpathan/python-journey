from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    """Handles displaying and updating the game score."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)         # Position at top of screen
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        """Display the current score."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Display 'GAME OVER' message at screen center."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score by 1 and refresh display."""
        self.score += 1
        self.clear()
        self.update_scoreboard()
