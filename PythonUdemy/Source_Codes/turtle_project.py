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