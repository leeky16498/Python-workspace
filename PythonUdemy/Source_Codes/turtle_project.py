# from turtle import *

# timmy_turtle = Turtle()
# timmy_turtle.shape("turtle")
#
# for i in range(3):
#     timmy_turtle.forward(100)
#     timmy_turtle.right(90)
#
# timmy_turtle.forward(100)
#
# done()
# # 정사각형 그리기 완료

# new_timmy = Turtle()
# new_timmy.shape("turtle")
# new_timmy.color("red", "blue")
#
# for i in range(4):
#     for j in range(20):
#         new_timmy.penup()
#         new_timmy.forward(5)
#         new_timmy.pendown()
#         new_timmy.forward(5)
#     new_timmy.right(90)
#
# new_timmy.hideturtle()
#
# done()
# 점선 정사각형 그리기 완료.

# ## 모듈을 임폴트하고, 패키지 설치하고, 별칭 사용하기.
# from turtle import *
# 다만 이렇게 하면 메서드의 모듈을 정확하게 찾아보기가 매우 힘들다.
# import turtle as tur
# # 다음과 같이 타입 앨리어싱도 가능합니다.
# timmy_turtle = tur.Turtle()

# 별을 붙여주시면 모듈 내 모든 속성과 메소드를 사용 가능하다.
# 말하자면 별도의 인스턴스 접근 없이 바로바로 메서드 사용이 가능하다는 것이다이.

# import turtle as tur
# t = tur.Turtle()
# t.shape("turtle")
#
# for i in range(3, 11):
#     for j in range(i):
#         angle = 360/i
#         t.forward(100)
#         t.right(angle)

## 터틀 다양한 도형 그리기 완료

from turtle import Turtle, Screen

tim = Turtle()
src = Screen()
def move_forward():
    tim.forward(10)

src.listen()
src.onkey(key="space", fun=move_forward)
## 보다시피 함수는 타입으로서 인자로 전달이 가능하다.
## 파이썬에서 고차함수란 것은 함수를 매개변수로 받는 함수를 고차함수라고 말한다.

src.exitonclick()

## 소수 체크 프로그램 ##

# n = int(input("Please give me the number, I will check whether the number is prime or not."))
# print("number we got is " + str(n))
#
# def prime_checker(number):
#     a = 0
#
#     for i in range(1, number):
#         if number % i == 0:
#             a += 1
#
#     print(a)
#
#     if a >= 2:
#         print("The number is not prime number")
#     else:
#         print("The number is prime number.")
#
# prime_checker(n)

### 비밀 경매 프로그램 코딩 ###

# from replit import clear
# from time import *
# import math

# user_info = {}

# for i in range(3):
#     user_name = input("What is your name?")
#     user_price = int(input("What is your price?")) 
#     user_info[user_name] = user_price
#     clear()

# print(user_info)

# prices = list(user_info.values())
# users = list(user_info.keys())

# winner_price = max(prices)
# print(winner_price)
# ## 배열에서 최대값 조회

# winner_price_index = prices.index(winner_price)
# print(winner_price_index)
# ## index 메서드를 통해 최대값 인덱스를 조회

# winner_user_name = users[winner_price_index]
# print("Winner of bid is " + winner_user_name)

## 경매 프로그램 코딩 완료

from inspect import isgenerator
from secrets import choice
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)

colors = ["red", "blue", "yellow", "black", "green", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
velosity = [10, 20, 30, 20, 10]
turtles = []

for index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_position[index])
    turtles.append(new_turtle)

print(turtles)

is_game_end = False

while not is_game_end:
    for index in range(len(turtles)):
        turtle = turtles[index]
        turtle.forward(choice(velosity))

        if turtle.pos()[0] == 200:
            is_game_end = True
            print("The game end, winner is " + turtle.pencolor())


screen.exitonclick()