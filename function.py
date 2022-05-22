def open_account(): #함수 정의는 def라는 키워드와 ()클로저로 정의해준다.
    print("새로운 계좌가 생성되었습니다.")

open_account()

#파라미터를 어떻게 대입하는지 알아봅세다.

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}입니다.".format(balance + money))
    return balance + money

balance = 0
balance = deposit(100, 10)
print(balance)

def withdraw(balance, money):
    if balance < money:
        print("돈이 부족합니다.")
        return balance
    else:
        print("출금이 완료되었습니다. 잔액은 {0}입니다.".format(balance - money))
        return balance - money

balance = 100
balance = withdraw(balance, 20)
print(balance)

def withdraw_night(balance, money):
    commission = 10 # 수수료 10원
    return commission, balance - money - commission


balance = withdraw_night(balance, 10)
print(balance)
#무섭다...그냥 자유롭게 되게 자유롭게 자료형 통제가 가능하다...이 언어 미쳤네 ㅋㅋㅋㅋㅋ

def profile(name, age, main_lang):
    print("이름 : {0}, 나이 : {1}, 주사용 언어 : {2}"\
        .format(name, age, main_lang))
        #역 슬래시 하고 저렇게 명시를 해주게 되면 그냥 같은 한줄의 코드이다.

profile("유재석", 20, "파이선")
profile("김태호", 25, "자바")

#만약 파라미터에 기본값을 설정하고 싶다면?

def profile1(name, age = 20, main_lang = "Python"):
    print("이름 : {0}, 나이 : {1}, 주사용 언어 : {2}"\
        .format(name, age, main_lang))
        #역 슬래시 하고 저렇게 명시를 해주게 되면 그냥 같은 한줄의 코드이다.

profile1("유재석")
profile1("김태호")

# 키워드 값을 활용한 함수

def profile2(name, age, main_lang):
    print(name, age, main_lang)

profile2(name = "유재석", main_lang="파이선", age = 25)
#단순하게 키워드에 해당하는 값이 순서가 섞여도 자연스럽게 잘 들어가게 된다.


# 가변인자 함수 호출
# def profile4(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile4(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()
    #다음과 같이 *표를 해주게 되면 가변 인자로 무엇이든 원하는 만큼 대입을 해주는 것이 가능하다.

profile4("유재석", 20, "자바", "자바", "자바", "자바", "자바")
profile4("김태호", 23, "자바", "자바")
