print("Python" + "Saha")
print("python", "saha")

print("python", "saha", sep = ",")
# 3번 코드와 같은 경우에는 python,saha를 출력해준다.
print("python", "saha", "korea", sep = " vs ")
#sep키워드를 통해서 분리 기호를 지정해줄 수 있다.

print("python", "java", sep = ",", end="? ")
print("뭐가 가장 재미있을까요?")
#이렇게 해주게 되면, 한줄로 쭉 출력이 된다. end키워드의 의미는 문장의 끝을 지정해주는 것이다. 기존에는 기본으로 줄바꿈이 들어가있다.

# import sys

# print("python", "java", file=sys.stdout)
# print("python", "java", file=sys.stderr)

# 출력포맷

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items():#items()해주면 키와 밸류를 쌍으로 튜플로 보내준다.
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep =  ":")
    #8칸을 보장하고 왼쪽정렬을 해달라.
    #스코어는 4칸을 확보하고 오른쪽 정렬을 해달리.

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    #이렇게 한다. 지필을 쓰면 3칸을 확보하고 출력을 하는데 빈 공간은 0으로 채워달라. 라는 기능임.

#표준 입력에 대해서 알아보자.
answer = input("아무값이나 입력해주십시오.")
print("입력하신 값은" + answer + "입니다.")
#표준 입력의 리턴값은 기본적으로 전부 str타입을 따른다.