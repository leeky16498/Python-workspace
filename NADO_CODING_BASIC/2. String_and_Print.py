### 문자열과 문자열 보간법, 출력함수사용 ###

sentence = "나는 소년입니다" # sentence라는 변수에 string 값을  "할당" 해준다.
print(sentence)
sentence2 = "파이선은 쉬워요"
print(sentence2)


sentence3 = """
나는
파이선과
스위프트 모두
다 좋아합니다.
"""
print(sentence3)
# 큰, 작은 따옴표 3개를 사용하면, 긴 줄의 주석 처리가 가능하다.

python = "Python is amazing"
print(python.lower())# 할당된 문자열을 전부 소문자 처리 한다.
print(python.upper())# 할당된 문자열을 전부 대문자 처리 한다.
print(python[0].isupper()) # 할당된 문자열의 대소문자 여부를 bool값으로 받을 수 있다.
# python[0]을 통해서 문자열의 첫 어절을 인덱스로 조회 가능하다.

print(len(python))
# len메소드를 통해 문자열의 count를 리턴해준다. 스위프트의 .count프로퍼티와 역할이 비슷하다.

print(python.replace("Python", "java"))
# replace메서드를 통해서 값을 조회하고 바꿀 수 있다.
# 앞에 찾을 문자열, 뒤에 바꿀 문자열 해주고 출력해준다.

index = python.index("n")
print(index)
# 해당되는 문자열의 인덱스 숫자를 리턴해준다.
# 해당되는 문자열이 없으면 리턴해버린다.

index = python.index("n", index + 1)
print(index)
# 이렇게 해주면 값은 값을 가지고 있는 2번째 인덱스를 리턴해준다.
# 지금은 python의 n 5 값을 하나 건너서 amazing의 n의 인덱스인 15를 리턴해주고 있다.

print(python.find("n"))
# find method이다. 이렇게 해주면 문자나 문자열의 인덱스를 리턴해준다.

print(python.find("java"))
print(python.find("amazing"))
# 찾는 문자열이 있는 경우 첫 문자 (이경우 "a")가 시작하는 인덱스를 리턴해준다.
# 원하는 문자열이 없으면 -1을 리턴한다.

print(python.count("n"))
# 해당되는 문자열이 얼마나 들어가는지에 대해서 체크가 가능하다.

print("a" + "B") # 얘는 스페이스가 없음
print("a", "b")# 얘는 스페이스가 있음

print("나는 20살입니다.")
print("나는 %d살 입니다" % 20)
# 단 이 경우는 퍼센트 뒤에 반드시 정수값만 넣을 수 있다.

print("나는 %s을 좋아해요" % "파이선")
# 이 경우는 문자열을 보간해준다.

print("Apple은 %c로 시작해요" % "A")
# 이는 문자열이 아닌 문자 하나를 받아온다.

print("나는 %s입니다요." % 20)
# s%는 와일드카드 패턴이다, 모든 자료형을 담을 수 있음.

print("나는 %s와 %s를 좋아해요" % ("파랑색", "빨간색"))
# 파라미터가 순서대로 들어간다.

print("나는 {}살입니다.".format(20))
# 괄호 안에 20이 들어간다.
print("나는 {}과, {}를 좋아해요".format("파란", "red"))
# 이렇게 해주면 순서대로 파라미터가 들어간다.단 함수 안에서 메소드로 구현을 해주게 된다.

print("나는 {1}과, {0}를 좋아해요".format("파란", "red"))
# 인덱스를 꼬아서 해주고 싶으면 인덱스를 직접 넣어서 해주면 된다.

print("나는 {age}이며, {color}을 좋아해요.".format(age = 20, color = "빨간"))
# 가장 보편적인 방법이기도 하다. 파라미터를 넣어주어도 되고, 포맷 내부의 인덱스를 넣어주어도 된다.
# 이렇게 직관적으로 연관값을 통해서 사용이 가능해진다.

age = 20
color = "빨간색"
print(f"나는 {age}이며, {color}을 좋아해요.")
# f키워드와 함께 써주면 이렇게 해주게 되면 전역 변수의 값을 넣어주게 된다.

print("백문이 불여일견 \n백견이 불여일타")
# \n을 해주면 줄바꿈을 해서 출력해주는 것이 가능하다.

print("저는 '나도코딩' 입니다.")
print('저는 "나도코딩" 입니다.')
print("저는 \"나도코딩\" 입니다.")

#역슬러시 따옴표 해주면 문장 내 기호로 사용이 가능하다.
#문장 내에서 \\두번 써주면 문장내에서 \로 표현이 된다.
#\r해주면 커서를 맨 앞으로 이동시켜 준다.

print("red apple\rpine")
#이렇게 해주면 pineapple이 출력된다.
#\b는 백스페이스 역할로 한 글자를 지워준다.

print("Redd\bApple")
#redApple을 출력하게 된다.

# \t : 탭 역할을 한다.
print("Red\tApple")

url = "http://naver.com"
my_str = url.replace("http://", "")
print(my_str)
my_str = my_str[:my_str.index(".")] 
# 여기에서 쓰인 [0:0] 연산자는 범위 인덱스 연산자이다.
#[:3] : 이렇게 써주면 처음부터 인덱스 3까지의 문자열을 가져온다.
#[3:] : 이렇게 해주면 인덱스 3부터 마지막까지의 문자열을 가져온다.

print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# 문자열끼리도 연산자를 통해 처리가 가능하지만, 자료형 변환이 필요한 경우에는 키워드를 통해서 래핑을 해줘야 한다.

print(password)
print("{0}의 비밀번호는 {1}입니다.".format(url, password))