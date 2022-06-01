from turtle import Turtle

class Walker(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black") 
        self.shape("turtle")
        self.penup()
        self.right(-90)
        self.goto(0, -370)
        self.y_move = 20

    def move(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)
    
        
