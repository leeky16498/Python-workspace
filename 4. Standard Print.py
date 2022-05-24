### 출력함수 심화 ###

print("Python" + "Saha")# 문자열을 합쳐주는 개념이다.
print("python", "saha")

print("python", "saha", sep = ",")
# 3번 코드와 같은 경우에는 python,saha를 출력해준다.

print("python", "saha", "korea", sep = " vs ")
# sep키워드를 통해서 분리 기호를 지정해줄 수 있다.
# 사이마다 sep이라는 키워드가 들어가며 출력된다.

print("python", "java", sep = ",", end= "?")
print("뭐가 가장 재미있을까요?")
#이렇게 해주게 되면, 한줄로 쭉 출력이 된다. end키워드의 의미는 문장의 끝을 지정해주는 것이다. 기존에는 기본으로 줄바꿈이 들어가있다.
#다음과 같은 경우 1, 2번 프린트가 연결되어 출력이 들어온다.

# import sys

# print("python", "java", file=sys.stdout)
# print("python", "java", file=sys.stderr)

### 출력포맷(정렬, 

scores = {"수학" : 0, "영어" : 50, "코딩" : 100} # 딕셔너리로 리턴해준다.
for subject, score in scores.items():#items()해주면 키와 밸류를 쌍으로 튜플로 보내준다.
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep =  ":") # ljust를 쓰면 왼쪽정렬, rjust를 쓰면 오른쪽정렬
    # 8칸을 보장하고 왼쪽정렬을 해달라.
    # 스코어는 4칸을 확보하고 오른쪽 정렬을 해달리.

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    #이렇게 한다. zfill을 쓰면 3칸을 확보하고 출력을 하는데 빈 공간은 0으로 채워달라라는 기능이다.

#표준 입력에 대해서 알아보자.
answer = input("아무값이나 입력해주십시오.")
print("입력하신 값은" + answer + "입니다.")
# 표준 입력의 리턴값은 기본적으로 전부 str타입을 따른다.


# 다양한 출력 포맷들

#1. 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: > 10}".format(500))

#2. 양수일 땐 +로 표시, 음수일 땐 - 로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#3. 왼쪽 정렬을 하고, 빈칸을 _ 로 채운다.
print("{0:_<10}".format(500))# 양음의 구분이 없다.
print("{0:_<+10}".format(500))# 양음의 구분이 있다.

#4. 3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000))

#5. 3자리마다 콤마를 찍어주기와 플러스 마이너스 부호 구분해보기
print("{0:+,}".format(10000000))

#6. 3자리마다 콤마를 찍어주는데 부호도 붙이고, 자리수도 확보한다. 돈이 많으면 기분이 좋으니까 빈자리는^표시로 채워본다.
print("{0:^<+30,}".format(1000000000000))

#6. 소숫점 출력하기!
print("{0:f}".format(5/3))

#7. 소숫점 특정자리수(2자리와 반올림) 까지 출력하기!
print("{0:.2f}".format(5/3))# .2f라는 키워드 사용에 주목한다.