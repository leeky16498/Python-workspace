
### 흐름 제어구문에 대해서 알아본다(if, elif, else) ###


# weather = "미세먼지"

weather = input("오늘 날씨 어떤가요?")
#인풋 메서드를 사용하면 값을 입력 받는다. 그리고 항상 문자열로 받아온다.
#그래서 해당 메서드를 통해서 값을 받은 경우 자료형을 int, float등으로 바꾸고 싶을땐 반드시 래핑을 해줘야 한다.

if weather == "비" or "눈": # 다음과 같이  or를 통해서 조건에 대한 통제가 가능하다. 교집합이면 and 를 쓴다.
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요.")

temp = int(input("온도가 어떤가요"))
#문자로 받은 데이터 자료형을 정수형으로 변경시킨다.

if 30 <= temp:
    print("너무 덥네요!")
elif 10 < temp and temp < 30:
    print("그럭저럭 괜찮네여")
else:
    print("너무 춥네요 나가지 말아주세요!")

    