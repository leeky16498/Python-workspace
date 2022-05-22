print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")

for wating_no in [0, 2, 2, 5, 4]:
    print("대기번호 : {0}".format(wating_no))

#리스트 내 값들에 대해서 하나씩 돌아가면서 인덱스 순서에 따라서
# 파라미터로 넣어주고 순서대로 출력해준다.

for wating_no1 in range(1, 5):
    print("대기번호 : {0}".format(wating_no1))
#범위를 지정해서 반복문을 지정해줄 수 있다. format보간법을 통해서 데이터를 입력해줄 수 있다.


starbucks = ["아이언맨", "토르", "아이엠그루트"]

for customer in starbucks:
    print("스타벅스에는 {0}의 커피가 준비되었습니다.".format(customer))


#while반복문에 대해서 공부해보자.

customer = "토르"
index = 5

while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피 버렸습니다.")


# customer = "아이언맨"

# while True:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

#이렇게 하면 무한 루프를 돌게 된다. while구문은 false가 되는 순간에 종료하고 나오게 된다.

# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 무엇인가요?")

#인풋을 통해서 값에 체크되면 while구문을 탈출하게 된다.


#continue 와 break에 대해서 알아본다.

absent = [2, 5]
nobook = [7]

for student in range(1, 11):
    if student in absent:
        continue #이 조건에 대해서는 반복루프를 한 번 건너뛴다.
    elif student in nobook:
        print("오늘 수업 여기까지, {0}는 교무실로 와".format(student))
        break # 반복문을 탈출해버린다.
    print("{0}야 책을 읽어보거라".format(student))


student = [1, 2, 3, 4, 5]

print(student)

student = [i+100 for i in student]
print(student)
#이렇게 해주면 101, 102, 103, 104, 105가 배열에 들어가있다.

students = ["Ironman", "Thor", "I am groot"]
students_int = [len(i) for i in students]
print(students_int)
# 7, 4, 10을 출력한다.

students_upper = [i.upper() for i in students]
print(students_upper)
#전부 대문자로 된 배열을 리턴해준다.

from random import *

cnt = 0 # 총 탑승 승객

for i in range(1, 51):
    time = randrange(5, 51)
    if  5 <= time <= 15:
        print("[0] {0}번쨰 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번쨰 손님 (소요시간 : {1}분)".format(i, time))