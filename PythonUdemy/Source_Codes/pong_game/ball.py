from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 20
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1 #벽에 부딫히면 방향을 틀어준다.
    
    def bounce_x(self):
        self.x_move *= -1
    
    def reset(self):
        self.goto(0,0)
        self.move()
        self.bounce_x()