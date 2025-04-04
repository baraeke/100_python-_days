from turtle import Turtle

# Constants for font styles
FONT_1 = ('Courier New', 13, 'normal')
FONT_2 = ('Courier New', 30, 'bold')
FONT_3 = ('Courier New', 15, 'bold')
ALLIGNMENT = 'center'


with open("data.txt", "r") as file:
    highscore = int(file.read())

class Score(Turtle):
    """Manages the scoreboard and player score."""

    def __init__(self):
        """Initializes the score display."""
        super().__init__()
        self.score = 0
        self.highscore = highscore
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        """Updates the score display on the screen."""
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALLIGNMENT, font=FONT_1)

    def score_update(self):
        """Increments the score and updates the scoreboard."""
        self.score += 1
        self.update_score()

    def reset(self):
        """Resets the score and updates the high score if necessary."""
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()
