#지역변수와 전역변수에 대해서 알아본다.

gun = 10

def checkpoint(soldiers):
    # gun = 20 # 이 친구가 지역변수로서 초기화를 해줘야 한다. 만약 안해주면 오류가 난다.
    global gun # 전역변수 gun을 함수에서 쓰겠다 라는 의미이다.
    gun = gun - soldiers
    print(gun)

checkpoint(2)

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print(gun)
    return gun
    # 파라미터 자체를 받아서 지역변수로 사용후 그 리턴 값을 다시 전역변수에 할당하여 재사용도 가능하다.

gun = checkpoint_ret(10, 7)

