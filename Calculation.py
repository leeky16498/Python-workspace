print(1+1)
print(3-2)
print(6/3)
print(2**3)
# 이렇게 해주면 2에 3승해서 8이 나온다
print(5%3)
# 얘는 비슷하게 나머지 연산자이다.
print(10//3)
# //는 몫을 출력해준다.
print(4 >= 7)
# 스위프트에 있는 연산자들과 비슷하다.
print(3==3)
print(3+4 == 7)
print(1 != 3)
print(not(1 != 3))
# not, ! 둘다 모두 부울 값에 대한 단항 연산자로 역할 가능하다.
print((3 > 4) and (3 < 5)) 
print((3 > 4) & (3 < 5)) 
print((3 > 4) or (3 < 5))  
print((3 > 4) | (3 < 5)) 

print(5>4>3)
print(5>4>7)

# 수식 표현이 가능하다.
print(3+2*4)
# 수식 표현에 있어서는 수학의 연산 처리 순서를 따른다.

number = 2+3*4
print(number)
number += 2
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %= 2
print(number)

# 숫자 처리 함수

print(abs(-5))
# 절대값을 나타내는 함수이다.
print(pow(4, 2))
# 4의 2승을 해준다
print(max(5, 12))
# 최대값을 식별해준다.
print(min(5, 12))
# 최소값을 나타내준다
print(round(3.14))
# 반올림을 해준다.

 # from math import * // 다음과 같이 쓰면 math 라이브러리 모듈을 사용하겠다는 명령어이다.
 # print(floor(4.99)) 내림.4
 # print(ceil(3.14) 올림
 # print(sqrt(16)) 제곱근

# from random import *

# print(random())
# 이렇게 해주면 랜덤함수를 통해 난수를 뽑아낼 수 있다.
# 0.0 이상 1.0 미만의 임의의 값을 생성해준다.
# print(random()*10)
# 이렇게 해주면 0.0에서 10.0 미만의 값을 생성해 준다.
# 근데 나는 뒤에 소수점을 가지기 싫다.
# print(int(random()*10))이렇게 해주면 정수형 자료형으로 바뀌므로 0에서 10사이의 자연수를 준다.

# print(int(random()*10) + 1)
# 이렇게 해주면 1에서 10 사이의 랜덤값을 생성한다.
# 로또 값을 생성해보자
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

