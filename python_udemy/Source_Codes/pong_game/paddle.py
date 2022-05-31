from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
    
    def go_up_down(self, xcor, ycor):
        self.goto(xcor, ycor)
        
        
    def controller_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def controller_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)