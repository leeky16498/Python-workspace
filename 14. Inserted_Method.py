### 내장함수 개념 ### 

# 내장함수는 별도의 import없이 바로 사용 가능한 파이선 자체로 소유하는 메서드와 프로퍼티를 의미한다.


# input함수 : 사용자 입력을 받는 함수

# language = input("좋아하는 언어가 뭔가요?")
# print("{0}은 매우 좋은 언어입니다.".format(language))

# dir 함수 : 어떤 객체를 넘겨주었을 때 그 객체가 어떤 변수와 함수를 가졌는지 표시해주는 내장함수
print(dir())
import random # 외장함수
print(dir())
import pickle
print(dir())

print(dir(random))
# 객체가 가지는 모든 항목들을 알려준다.

lst = [1, 2, 3]
print(dir(lst))
#list에서 사용가능한 모든 것들이 나온다.

name = "이경윤"
print(dir(name))
# 네임에게 반영 가능한 객체 속성들이 나온다.