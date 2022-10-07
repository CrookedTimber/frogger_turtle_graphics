from turtle import Turtle
import random

from settings import HEIGHT, WIDTH

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SHAPES = ["square"]
CAR_LENGTHS = [2]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shape(random.choice(SHAPES))
        self.color(random.choice(COLORS), random.choice(COLORS))
        self.shapesize(stretch_len=random.choice(CAR_LENGTHS))
        self.spawn()

    def move(self):
        self.forward(MOVE_INCREMENT)

    def spawn(self):
        x_location = random.randint(-(WIDTH / 2 - 20), (WIDTH / 2 - 20))
        y_location = random.randint(-(HEIGHT / 2 - 80), (HEIGHT / 2 - 80))
        self.goto(x_location, y_location)

    def back_to_screen(self):
        self.goto(WIDTH / 2, self.ycor())
