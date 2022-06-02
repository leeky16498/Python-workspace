### 연산자 정의 ###

## 연산자 깃허브 동기화 여부 체크 ##
print(1+1)# 덧셈 연산자
print(3-2)# 뺄셈 연산자
print(6/3)# 나누기 연산자
print(2**3)# 제곱 연산자, 이렇게 해주면 2에 3승해서 8이 나온다
print(5%3)# 나머지 연산자
print(10//3)# 몫 연산자
print(4 >= 7)# 중위 연산자, 4가 7보다 크거나 같은가?, bool 값을 리턴해준다.(비교 연산자)
print(3==3)# == 3이 3과 같다면, bool
print(3+4 == 7)# 3+4가 7이라면, bool
print(1 != 3)# ! : not 연산자, 대비연산자이다. 1이 3이 아니라면, 의미
print(not(1 != 3))# not래퍼, ! 둘다 모두 부울 값에 대한 단항 연산자로 역할 가능하다.
print((3 > 4) and (3 < 5))#연산자의 교집합 and 키워드 또는 & 엠퍼센드로 처리 가능
print((3 > 4) & (3 < 5)) 
print((3 > 4) or (3 < 5))#합집합 연산자 or 키워드 또는 |로 처리 가능 
print((3 > 4) | (3 < 5)) 

print(5>4>3)# 판단 여부에 따라서 연속된 연산자 사용도 가능함.
print(5>4>7)# 하나라도 틀린다면 False를 리턴한다.

print(3+2*4)# 수식 표현에 있어서는 수학의 연산 처리 순서를 따른다.(곱셈, 나눗셈에서 덧셈 뺄셈 순)

number = 2+3*4
print(number)
number += 2 # number = number + 2(2를 더한 값을 다시 number에 할당한다. 라는 줄임 연산자)
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %= 2
print(number)


### 숫자 처리 함수 ###

print(abs(-5))# 절대값을 나타내는 함수이다.
print(pow(4, 2))# 4의 2승을 해준다
print(max(5, 12))# 최대값을 식별해준다.
print(min(5, 12))# 최소값을 나타내준다
print(round(3.14))# 반올림을 해준다.

from math import * 
# 다음과 같이 쓰면 math 라이브러리 모듈을 사용하겠다는 명령어이다. 파이썬은 줄바꿈에 민감하다. 반드시 정렬해야한다.
# 의미 : math 모듈에 있는 모든 메서드와 프로퍼티를 import 한다. 라는 의미이며 *은 all 생성자 역할을 한다.
# * 대신에 구체적인 메서드 리스트를 명시해주면 해당 메서드들만 사용도 가능하다.

print(floor(4.99)) #내림 : floor
print(ceil(3.14)) # 올림 : ceil
print(sqrt(16)) # 제곱근 : sqrt


### 랜덤 함수 ###
from random import *
# 랜덤 외장함수의 모든 메서드를 import 한다.
# 외장함수의 리스트는 pypi. 홈페이지에서 다양하게 확인이 가능하며, 모듈 설치를 해줘야 사용이 가능하다.

print(random())
# 이렇게 해주면 랜덤함수를 통해 난수를 뽑아낼 수 있다.
# 0.0 이상 1.0 미만의 임의의 값을 생성해준다.

print(random()*10)
# 이렇게 해주면 0.0에서 10.0 미만의 값을 생성해 준다.
# 근데 나는 뒤에 소수점을 가지기 싫다.

print(int(random()*10))
# 이렇게 해주면 정수형 자료형으로 바뀌므로 0에서 10사이의 자연수를 준다.

print(int(random()*10) + 1)
# 이렇게 해주면 1에서 10 사이의 랜덤값을 생성한다.


### 로또 값을 생성해보자
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)

# 이렇게 해주면 6자리 로또 번호가 생성된다.
# print(randrange(1, 46)) 이건 1 ~ 45 사이의 미만 값을 생성하라는 의미임
# print(randrange(1, 46)) 이건 1 ~ 45 사이의 미만 값을 생성하라는 의미임
# print(randrange(1, 46)) 이건 1 ~ 45 사이의 미만 값을 생성하라는 의미임
# print(randrange(1, 46)) 이건 1 ~ 45 사이의 미만 값을 생성하라는 의미임
# print(randrange(1, 46)) 이건 1 ~ 45 사이의 미만 값을 생성하라는 의미임
# print(randrange(1, 46)) 이건 1 ~ 45 사이의 미만 값을 생성하라는 의미임

# print(randint(1, 45)) 얘는 1에서 45사이의 값 생성이 가능하다. 얘는 양 끝을 포함한다.

