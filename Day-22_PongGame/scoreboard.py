from turtle import Turtle

class Scoreboard(Turtle):
    """Displays and updates the score for both players."""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0     # Left player score
        self.r_score = 0     # Right player score
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear and rewrite the current score."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Increase left player's score."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increase right player's score."""
        self.r_score += 1
        self.update_scoreboard()
