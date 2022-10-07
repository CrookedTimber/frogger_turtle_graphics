import time
from turtle import Screen
from settings import HEIGHT, WIDTH, SPEED
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

frog = Player()
game_score = Scoreboard()

screen.onkey(key="Up", fun=frog.up)

screen.listen()

cars = []

game_speed = SPEED


def produce_cars(car_number):
    for starting_cars in range(car_number):
        new_car = CarManager()
        cars.append(new_car)


produce_cars(10)

game_is_on = True

while game_is_on:
    time.sleep(game_speed)
    screen.update()

    if frog.ycor() > HEIGHT / 2 - 50:
        frog.new_round()
        game_score.increase_level()
        produce_cars(2)
        game_speed *= 0.8
        for car in cars:
            car.spawn()

    for car in cars:
        car.move()
        if car.xcor() < -(WIDTH / 2):
            car.back_to_screen()
        if car.distance(frog) < 20:
            game_is_on = False
            game_score.game_over()


screen.exitonclick()
