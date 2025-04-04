from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Manages the display and updating of the player's score."""
    
    def __init__(self):
        """Initializes the scoreboard with a starting score of 0."""
        super().__init__() 
        self.score = 0  
        self.hideturtle()
        self.penup()
        self.goto((0, 270))
        self.write(f"Score: {self.score}", move=False, align="center", font=FONT)

    def score_update(self):
        """Clears the previous score and updates it by increasing it by 1."""
        self.clear()  
        self.score += 1 
        self.write(f"Score: {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        """Displays the final score at the center of the screen when the game ends."""
        self.clear() 
        self.goto((0, 0)) 
        self.write(f"GAME OVER", move=False, align="center", font=FONT)
        self.goto((0, -40))
        self.write(f"Final score: {self.score}", move=False, align="center", font=FONT) 