from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.l_player_score = 0
        self.r_player_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.display_score()

    def display_score(self):
        """Displays the current score at the top center."""
        self.clear()  
        self.write(arg=f"{self.l_player_score} : {self.r_player_score}",
                   move=False, align="center", font=("Courier", 26, "bold"))


    def game_over(self):
        """Displays the game over message and final score."""
        self.goto(0, 50)  
        self.write(arg="GAME OVER", move=False, align="center", font=("Courier", 30, "bold"))

        self.goto(0, 0)
        self.write(arg=f"Final Score: Left player {self.l_player_score} : {self.r_player_score} Right player",
                   move=False, align="center", font=("Courier", 15, "bold"))

    def l_score(self):
        self.l_player_score += 1
        self.display_score()

    def r_score(self):
        self.r_player_score += 1
        self.display_score()