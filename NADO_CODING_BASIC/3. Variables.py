### 지역변수와 전역변수 ###

gun = 10
# 지역변수 : 함수나 클래스 안에서 선언된 변수를 의미하며, 외부에서 사용될 수 없고, 인스턴스를 생성해야 사용이 가능하다.
# 전역변수 : 함수나 클래스에 속하지 않는 변수를 의미하며 전체적으로 사용이 가능하다.

def checkpoint(soldiers): # 함수를 선언할때는 def 키워드를 사용해서 선언하게 되며(안에는 파라미터가 들어가게 된다.)
    global gun # 전역변수를 함수나 클래스 내에서 구분지어 선언할때는 앞에 global 키워드로 선언해준다.
    gun = gun - soldiers # 아래에서 쓰이는 gun은 전역변수 gun이 쓰이게 된다.
    print(gun)

checkpoint(2)

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print(gun)
    return gun
    # 파라미터 자체를 받아서 지역변수로 사용후 그 리턴 값을 다시 전역변수에 할당하여 재사용도 가능하다.
    # 중요 포인트는 지역변수와 전역변수는 같지 않고, 다른 존재라는 것이며, 서로 접근할 때는 적절한 키워드를 명시해주어야 한다.

gun = checkpoint_ret(10, 7)
