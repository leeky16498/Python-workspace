
from turtle import Turtle, Screen
from walker import Walker
from car import Cars
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(800, 800)
screen.title("crossing game")
screen.tracer(0)

walker = Walker()
cars = []

def make_rand_cars():
    for number in range(1, 70):
        new_car = Cars()
        cars.append(new_car)

screen.listen()
screen.onkey(walker.move, "Up")

make_rand_cars()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    
    for car in cars:
        car.move()
        
        if car.xcor() >= 380:
            car.reset_location()
        
        if car.distance(walker) < 20:
            print("game over") 
    
    if walker.ycor() >= 380:
        
        for car in cars:
            car.velocity += 5
        
        walker.goto(0, -370)


screen.exitonclick()