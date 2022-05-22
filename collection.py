# 컬렉션 중 리스트를 알아본다

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
# 다음과 같이 리스트로 제작이 가능하다.
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)
print(subway.index("조세호"))
# 조세호의 인덱스를 찾아서 출력해준다.

subway.append("하하")
print(subway)
#append하면 항상 맨 뒤에 붙게 된다.

subway.insert(1, "정형돈")
print(subway)
#이렇게 원하는 인덱스에 직접 대입이 가능합니다.

subway.pop()
print(subway)
#pop을 해주게되면 가장 뒤에서부터 자동 삭제가 된다.

subway.append("유재석")
print(subway)
print(subway.count("유재석"))
#카운트를 통해서 얼마나 들어있는지 알 수 있다.

num_list = [1, 3, 2, 4, 6, 8, 5, 1]
num_list.sort()
print(num_list)
#소트 함수를 먹여주면 작은것부터 순서대로 정렬된다.
num_list.reverse()
print(num_list)
#큰 것부터 정렬이 된다.
num_list.clear()
#리스트의 모든 내용을 삭제해서 빈 배열을 리턴해준다.
#리스트는 자료형에 구애받지 않고 자유롭게 사용이 가능하다.
mix_list = ["조세호", 1, True]
print(mix_list)

#리스트의 확장도 가능하다.
num_list.extend(mix_list)
print(num_list)
#리스트를 하나로 합쳐주는 메소드이다. 익스텐드 메소드

#여기에서는 딕셔너리를 알아본다. 딕셔너리의 개념은 스위프트에서 제공하는 것과 동일하다.

cabinet = {3:"유재석"}
# 3 : 키, "유재석" : 밸류이다. 다음처럼 키와 밸류값을 저렇게 중괄호에 넣어서 만든다.
cabinet = {3:"유재석", 100:"김태호"}
#사전으로 구성된 리스트를 만들수도 있따.
print(cabinet[3])
#3번 키를 가진 값, 유재석이 출력된다.
print(cabinet.get(3))
#이렇게 해도 유재석 값을 가져온다.
# print(cabinet[45])
#런타임 오류가 나고 프로그램이 종료된다. 없는 키 값을 입력하는 경우 오류가 발생한다.
print(cabinet.get(45))
#겟을 사용하면 none을 출력해주고 프로그램이 종료되지 않는다. 일종의 옵셔널 바인딩과 비슷하다.
print(cabinet.get(45, "사용가능"))
#이렇게 하면 45를 조회해서 값이 없으면 45키 값을 사용가능으로 설정해준다.
print(3 in cabinet)
#키 값이 딕셔너리에 있으면 true값을 리턴해준다.


cabinet1 = {"A-3" : "유재석", "B-3" : "조새효"}
print(cabinet1["A-3"])

cabinet1["C-20"] = "조세호"
print(cabinet1)
#이렇게 하면 딕셔너리에 데이터 추가를 해줄 수 있다.
cabinet1["A-3"] = "김종국"
print(cabinet1)
#존재하는 키 값에 다음과 같이 값을 다시 세팅하면 값이 대체가 된다.

del cabinet1["A-3"]
print(cabinet1)
#del키워드를 입력하면 딕셔너리 데이터를 지울 수 있다.

print(cabinet1.keys())
print(cabinet1.values())
# 키 값만 출력하거나 밸류들만 출력할 수 있다.
print(cabinet1.items())
#이렇게 하면 키와 밸류값의 쌍으로 딕셔너리 아이템을 리턴해준다.
cabinet1.clear()
print(cabinet1)
#딕셔너리를 전부 클리어 시키고 포맷해버린다.


##튜플에 대해서 배워본다. 스위프트에서도 제공하는 특수 자료형이다.
menu = ("돈까스", "치즈까스")
print(menu[1])
print(menu[0])
#인덱스로 각 튜플 인덱스 값에 접근이 가능하다.


(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

#튜플 자체의 변수를 다음과 같이 자료형으로 선언이 가능하다.


#세트에 대해서 알아본다. 집합이라고도 하는데 중복이 안되고, 순서가 없다.

my_set = {1, 2, 3, 3, 4, 5, 5}
print(my_set)
java = {"유재석", "김태후", "양세형"}
python = set(["유재석", "박명수"])

# 자바와 파이선 모두가 가능한 교집합을 찾아보자
print(java&python)
print(java.intersection(python))
# 유재석이 출력된다.

#합집합(java 또는 python을 할 수 있는 사람)
print(java | python)
print(java.union(python))
#모든 개발자 리스트를 출력해준다. 물론 순서가 다르므로 매번 순서가 변한다.

# 차집합(자바는 할줄 알지만 파이선을 할지 모르는 사람)
print(java - python)
print(java.difference(python))

print("Git test")

#파이선을 할 줄 아는 사람이 늘어났다.
python.add("이경윤")
print(python)

#add키워드를 통해서 집합 값 추가가 가능하다.

#자바를 까먹었다.
java.remove("김태후")
#집합에서 해당 자료를 제거 가능하다.


##자료구조의 변경

menu = {"커피", "우유", "쥬스"}
print(menu, type(menu))
#type메서드는 자료형 타입을 출력해준다.

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))
#보는 것처럼 자료형으로 감싸주면 타입을 변경해줄 수 있다.

menu = set(menu)
print(menu, type(menu))
#다시 자료형을 지정해줄 수 있다.

from random import *

lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
#랜덤하게 값이 섞였다.
print(sample(lst, 1))
#리스트 중 렌덤하게 1개의 숫자를 출력하겠다.

users = range(1, 21)
#1부터 20까지의 숫자를 생성한다.
print(type(users))
users = list(users)
print(users)
#레인지 자료형이 리스트로 저장이 된다.

shuffle(users)
print(users)
#셔플 메서드를 통해서 유저를 섞었다.

winners = sample(users, 4)
print(winners)

print("==치킨 당첨자==")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("==축하합니다!==")
