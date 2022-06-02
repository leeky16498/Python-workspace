from numpy import multiply


def add(*args):
    a = 0
    for n in args:
        a += n
        
    return a

sol = add(1, 2, 3, 4, 5, 6)
print(sol)

## 튜플이므로 인덱스로 접근이 가능해진다. for example, args[0] = 1이다.
## 아스테릭스 키워드는 무한의 인자를 받아온다. 근데 숫자로 받아온다이.

def calculate(**kwargs):
    print(kwargs)
    #키워드 아규먼츠의 줄임말이다.
    
    for (key, value) in kwargs.items():
        print(key)
    
calculate(add=3, multiply=5)
#{'add': 3, 'multiply': 5} 다음과 같이 출력이 된다.
#따라서 위처럼 딕셔너리 컴프리헨션도 가능해진다.

def calculate(n, **kwargs):
    print(kwargs)
    
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculate(2, add=3, multiply=5)
## 25를 출력한다.


class Car:
    
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        
        ##get메서드는 에러처리가 가능하며, 런타임 오류로 인한 프로그램 종료를 발생시키지 않는다.
        
my_car = Car(make="Nissan", model="GTR")
print(my_car.model)