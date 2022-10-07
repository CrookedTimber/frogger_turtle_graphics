from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")
        self.color("brown", "green")
        self.shapesize(1.5, 1.5, 1.5)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def new_round(self):
        self.goto(STARTING_POSITION)
