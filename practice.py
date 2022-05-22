print(5)
print(-5)
print(3.14)
print(1000)
print(5+3)
print(2*3)
print(3*(3+1))
print('풍선')
print("나비")
print("z")
print("z"*9)
print(5>10)
# 샵으로 주석을 달아줄 수 있다.
print(5<10)
print(True)
print(False)
# 대문자로 트루 풜스를 써준다
print(not True)
print(not False)
print(not (5<10)) 
# 다음과 같다.
# 애완동물을 소개해 주세요

animal = "강아지"
name  = "연탄이"
age = 4
hobby = "산책"
is_Adult = age >= 3
# 위에는 변수를 선언해준 것들이다. 별도로 앞에 키워드는 안 붙은 상태이다.
# 아래에서는 변수의 보간법을 알 수 있다.

print("우리집 " + animal + " 이름은" + name + "에요")
print("연탄이는" + str(age) + "살이고, 산책을 정말 좋아합니다.")
print("연탄이는 어른일까요?" + str(True))

animal = "고양이"
# 다음과 같이 해주면 변수에 새로운 값을 할당해줄 수 있다.

'''
이렇게 해주면 여러문장 주석이 가능하다.
이렇게 엔터해서도 주석처리가 가능해집니다!!
control + /해주면 일괄 주석처리가 가능하다.(스위프트랑 비슷해))
'''

print("우리집 " + animal + " 이름은" + name + "에요")
print("연탄이는", age, "살이고, 산책을 정말 좋아합니다.")
print("연탄이는 어른일까요?", True)
# 다음과 같이 쉼표를 통해서 별도로 문자열 변환을 시도하지 않고도 보간법이 가능하다.
