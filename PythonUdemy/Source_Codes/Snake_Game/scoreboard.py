from turtle import Turtle
import time

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.title = "current scores"
        self.penup()
        self.score = 0
        self.write("Scores: " + str(self.score), True, align = "center")
        self.write((0, 280), True)
        self.hideturtle()