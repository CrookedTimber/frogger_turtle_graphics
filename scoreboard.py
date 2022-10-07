from turtle import Turtle

from settings import HEIGHT, WIDTH


FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.color("black")
        self.hideturtle()
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.goto(-(WIDTH / 2 - 40), HEIGHT / 2 - 80)
        self.write(
            f"Level: {self.level}",
            align="left",
            font=FONT,
        )

    def increase_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"GAME OVER",
            align="center",
            font=FONT,
        )
