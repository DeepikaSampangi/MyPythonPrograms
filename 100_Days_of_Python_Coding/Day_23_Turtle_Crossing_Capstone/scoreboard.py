from turtle import Turtle


FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-275, 275)
        self.updated_score()
        self.hideturtle()

    def updated_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
