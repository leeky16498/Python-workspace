# weather = "미세먼지"

weather = input("오늘 날씨 어떤가요?")
#인풋 메서드를 사용하면 값을 입력 받는다. 그리고 항상 문자열로 받아온다.

if weather == "비" or "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어여")

#파이선이 훨씬 조건적이지만 업무가 빠르다.
#표현도 대단히 직관적이다.

temp = int(input("온도가 어떤가요"))
#문자로 받은 데이터 자료형을 정수형으로 변경시킨다.

if 30 <= temp:
    print("너무 덥네요!")
elif 10 < temp and temp < 30:
    print("그럭저럭 괜찮네여")
else:
    print("너무 춥네요 나가지 말아주세요!")

    