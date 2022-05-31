from tkinter import Pack
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 800)
screen.title("Pong game")
screen.tracer(0)
## 애니메이션의 통제여부를 결정하는 메서드이다.

ball = Ball()
scoreboard = Scoreboard()

paddle1 = Paddle()
paddle1.penup()
paddle1.go_up_down(350, 0)

paddle2 = Paddle()
paddle2.penup()
paddle2.go_up_down(-350, 0)

screen.listen()
screen.onkey(paddle1.controller_up, "Up")
screen.onkey(paddle1.controller_down, "Down")

game_is_on  = True
game_point_right = 0
game_point_left = 0

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()
        
    # 패들과의 접촉을 체크해준다.
    if ball.distance(paddle1) < 20 and ball.xcor() > 340 or ball.distance(paddle2) < 20 and ball.xcor() < -340:
        ball.bounce_x()
    
    if ball.xcor() < -390:
        ball.reset()
        scoreboard.clear()
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()
    
    if ball.xcor() > 390:
        ball.reset()
        scoreboard.clear()
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()

