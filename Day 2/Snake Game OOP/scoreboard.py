from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.write(font=("ARIAL", 12, ""), arg=f"Score: {self.score}", align="center")

    def change_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}")

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(font=("ARIAL", 20, ""), arg="GAME OVER", align="center")
        self.goto(0, -10)
        self.write(font=("ARIAL", 12, ""), arg=f"Score: {self.score}", align="center")
