from turtle import Turtle
import time
import random

COLORS = ["blue", "red", "yellow", "green", "purple"]

class Cars(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.velocity = 10
        self.start_position()
    
    def start_position(self):
        self.penup()
        self.goto(random.randint(-300, 300), random.randint(-300, 300))
        
    def move(self):
        new_x = self.xcor() + self.velocity
        self.goto(new_x, self.ycor())

    def reset_location(self):
        self.goto(-390, self.ycor())