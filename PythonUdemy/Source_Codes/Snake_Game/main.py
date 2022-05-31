from turtle import Screen, Turtle
from scoreboard import Scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
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
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    # 벽에 꼬리와 머리의 충돌 여부를 체크한다.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        
    # 뱀의 머리가 몸과 부딫혔는지 체크하기.
    
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    
    # 슬라이싱을 해본다.[0:0] 다음과 같이 우리가 원하는 자료를 잘라서 가져온다.
    # 슬라이싱 간에[0:0:1] 해주면 1씩 건너뛰면서 가져온다.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
     
screen.exitonclick()