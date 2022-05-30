from turtle import Screen, Turtle
from scoreboard import Scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen() 
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update() 
    time.sleep(0.1)
    ## 뒤의 블럭이 앞의 블럭을 밀어내며 이동하도록 코딩함.
    snake.move()
    
    ## 먹이와의 충돌여부를 결정한다.
    ## 터틀의 distance 메서드를 통해서 좌표에 접근여부를 체크한다.
    if snake.head.distance(food) < 15:
        snake.add_new_body()
        scoreboard.increase_score()
        food.refresh()
        
screen.exitonclick()