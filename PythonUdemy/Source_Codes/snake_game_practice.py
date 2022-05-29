from turtle import Screen, Turtle, bgcolor
import time

screen = Screen()
screen.setup(600, 400)
screen.bgcolor("black")
screen.title("Snake Game")

turtles = []

for index in range(3):
    new_turtles = Turtle("square")
    new_turtles.penup()
    new_turtles.color("white")
    new_turtles.setpos(20*index, 0)
    turtles.append(new_turtles)

print(turtles)

is_game_end = False

while not is_game_end:
    for turtle in turtles:
        time.sleep(0.3)

        if turtle.pos()[0] == 300:
            is_game_end = True
   
            print("The game is over")
          

screen.exitonclick()
### 스네이크 제작 완료
