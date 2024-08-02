from turtle import Turtle

FONT = ("courier", 15, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.points = 0
        self.hideturtle()
        self.penup()
        self.setx(-140)
        self.sety(275)
        self.color("white")
        self.update()
        # self.write("Score: ", move=True, font=FONT)
        # self.color("white")
        # self.write(self.points, move=True, font=FONT)

    def change(self):
        self.points += 1
        self.update()

        # self.points += 1
        # self.clear()
        # self.setx(-50)
        # self.sety(275)
        # self.color("white")
        # self.write(f"Score: {self.points} High score: {self.highscore}", move=True, font=FONT)

    def update(self):
        self.clear()
        self.write(f"Score: {self.points} High score: {self.highscore}", move=False, font=FONT)

    def reset_score(self):
        if self.points > self.highscore:
            self.highscore = self.points
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.points = 0
        self.update()

    # def game_over(self):
    #     self.setx(-185)
    #     self.sety(-25)
    #     self.color("white")
    #     self.write("GAME OVER", move=True, font=("courier", 50, "bold"))
