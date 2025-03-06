from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = -1
        self.set_high_score()
        self.teleport(x=0, y=270)
        self.color("white")
        self.increase_score()


    def set_high_score(self):
        with open("high_score.txt") as high_score:
            self.high_score = int(high_score.read())


    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 20, "normal"))


    def game_over(self):
        self.home()
        self.write(arg="Game Over!", align="center", font=("Courier", 24, "normal"))
        if self.score > self.high_score:
            self.high_score = self.score

        with open("high_score.txt", mode="w") as high_score:
            high_score.write(f"{self.high_score}")
