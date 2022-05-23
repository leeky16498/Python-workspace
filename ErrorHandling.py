# 에러 처리에 대해서 공부해본다.(또는 예외 처리라고 한다.)
try: 
    print("나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자를 입력해주세여."))
    num2 = int(input("두 번째 숫자를 입력바랍니다."))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
    #try 부분을 실행하고 만약 에러가 발생하면 except 부분일 실행하게 된다.

except ValueError:
    print("값이 맞지 않아 에러가 발생했습니다.")
except ZeroDivisionError as err:
    print(err)
    #다음과 같이 에러 값을 변수에 받아서 그 내용을 프린트 해준다.


try:
    print("나누기 두번째 계산기 입니다.")
    nums = []
    nums.append(int(input("첫 수를 입력해보세요.")))
    nums,append(int(input("두번째 수도 입력해보세요.")))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except Exception as err:
    print("알 수 없는 에러데스!")
    print(err)
    #다음과 같이 exception을 통해서 기타 나머지 오류를 받을 수 있다.


## 일부러 에러를 발생시켜 본다.

## 스위프트랑 비슷하게, try키워드를 통해서 에러 발생가능성이 있는 함수에 대해 예외구문 처리를 한다.

## 사용자 정의 에러처리를 해보자.
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 수는?"))
    num2 = int(input("두 번째 숫자는?"))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("한자리 수만 입력하세요.")
except BigNumberError as err:
    print("빅넘버 에러데스")
    print(err)
finally:
    print("계산기를 이용해주시어 감사드립니다.")


## finally에 대해서 알아보자. 에러처리에서 에러가 생기든 안생기든 무조건 실행되는 defer같은 구문이다.
## 에러처리를 통해 런타임 오류를 미리 막을 수 있다.

class SoldoutError(Exception):
    pass

chicken = 10
wating = 1

while(True):
    try: 
        print("남은치킨 {0}".format(chicken))
        order = int(input("치킨 얼마나 주문하실건가요?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("대기번호 {0} 의 {1} 주문이 완료되었습니다.".format(wating, order))
            wating += 1
            chicken -= order
        if chicken == 0:
            raise SoldoutError
    except ValueError:
        print("잘못된 값을 입력했습니다.")
    except SoldoutError:
        print("치킨이 모자랍니다.")
        break #이를 통해서 반복문을 탈출한다.
