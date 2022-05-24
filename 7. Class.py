### 클래스 개념 ###

# 파이썬은 스위프트와 다르게 자료형을 일괄적으로 클래스로 연결지어 사용한다.
# 구조체 개념이 없는 것으로 판단된다. 이건 더 찾아볼 예정이다.

# 마린 : 공격유닛, 군인. 총을 쏠 수 있다.
from random import *

# 외장함수를 가져다 쓰는 중이다.
# 랜덤 외장함수를 인스톨 하고, 임폴트 하는데 *은 저 랜덤 모듈의 모든 프로퍼티와 메서드를 사용한다는 의미이다.

name = "마린"
hp = 40
damage = 5

print("{}유닛이 생성되었습니다.".format(name))
print("체력은{0}, 공격력은 {1}입니다.".format(hp, damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{}유닛이 생성되었습니다.".format(tank_name))
print("체력은{0}, 공격력은 {1}입니다.".format(tank_hp, tank_damage))

tank2_name = "탱크2"
tank2_hp = 150
tank2_damage = 35

print("{}유닛이 생성되었습니다.".format(tank_name))
print("체력은{0}, 공격력은 {1}입니다.".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다 : {2}".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# 클래스는 붕어빵 틀에 비유를 하게 되는데, 붕어빵 틀은 형태가 갖추어져 있다. 틀은 하나지만 붕어빵은 많이 만들 수 있다.
# 클래스는 사용자 정의 자료형이다.
# 아래에서 클래스로 정의 후 다시 만든다.

# 일반유닛 클래스
class Unit: # 키워드를 클래스로 명시해준다.
    def __init__(self, name, hp, damage, speed):
        # 파이썬에서는 self 파라미터도 전부 같이 넘겨주어야 한다.
        # 이 친구는 생성자 호출부분이다. 클래스 인스턴스를 생성할 때 호출이 되는 부분이다.
        # 다른 것들과 다르게 이 친구는  self 를 꼭 파라미터로 넘겨주어야 한다.
        self.name = name
        self.hp = hp
        self.damage = damage
        self.speed = speed

    def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
            .format(self.name, location, self.speed))
    #self는 클래스 객체 자체를 의미하며, self.name을 하게 되면 객체 내의 지역변수를 의미하게 된다.
    #함수 내에서 파라미터로 선언한 친구와는 다른 객체를 가지게 된다.

    
marine1 = Unit("마린", 40, 5, 10)
marine2 = Unit("마린2", 40, 5, 10)
tank1 = Unit("탱크", 140, 25, 10)
tank21 = Unit("탱크21", 140, 25, 10)

# 멤버변수 : 클래스나 함수 안에서 사용되는 변수들이 멤버변수이다.

# 레이스는 공중유닛인데 클로킹이 있는 친구이다.
wraith1 = Unit("레이스", 80, 5, 10)
print("클래스 외부 호출입니다. 유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.hp))
# 멤버변수를 .을 찍어서 호출이 가능하다.

# 다크 아칸이 마인드 컨트롤을 시도했다.
wraith2 = Unit("빼앗은 레이스", 80, 5, 10)
wraith2.clocking = True
# 지금 clocking이라는 변수는 없는데, 이렇게 자유롭게 클래스에 바로바로 객체에 추가 변수를 외부에서 할당해서 쓸 수 있다.

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


# if wraith1.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
# 이러면 오류가 나는데 해당 객체에 대해서만 적용이 되고 다른 모든 객체에 대해서는 적용이 안된다.



### 클래스의 상속 ###

# 클래스 옆에 ()안에 클래스 이름을 넣으면 해당 클래스를 상속받는다.
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, damage, speed)
        # 슈퍼 클래스 생성자를 받아온다.
        # 다중상속을 할 때는 하나하나 클래스의 이름을 명시해야 하며, 
        # 만약 하나의 클래스만 상속 시에는 super.__init__ 다음과 같이 생성자를 명시할 수 있다.
        # 다중 상속 중 super.__init__을 처리하게 되면 가장 마지막 클래스만 상속을 받게 된다.
        self.name = name
        # self.hp = hp(상속으로 처리 예정이다.)
        # self.damage = damage

    def attack(self, location): # 클래스 내에서 메소드 앞에서는 항상 self파라미터를 직접 나타낸다고 생각하자.
        print("{0} : {1} 방향으로 적군을 공격한다. [공격력 : {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16, 10)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)


## 클래스의 다중상속에 대해서 알아보자.

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다 : [속도 : {2}]"\
            .format(name, location, self.flying_speed))

# 두 클래스를 다중상속하였다.
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, flying_speed)
        Flyable.__init__(self, flying_speed)

    # 상속받은 함수에 대한 재정의는 override등의 키워드 별도 표현없이 똑같은 이름의 함수를 새롭게 정의해주면 된다.
    def move(self, location):
        print()
        self.fly(self.name, location)

# 발키리를 제작해본다.

valkirie1 = FlyableAttackUnit("발키리1", 250, 15, 5)
valkirie1.fly(valkirie1.name, "3시")

# 연산자 오버라이딩에 대해서 알아본다. 쉽게 말하면 상속받는 것들을 재정의하는 것이라고 보면 된다.

vulture = AttackUnit("벌쳐", 80, 10, 10)
vulture.move("11시")

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
battlecruiser.move("9시")


## 패스에 대해서 공부해본다.

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 의미는 일단 함수는 완성되지 않았지만 그냥 지나간다. 라는 의미이다.

# 서플라이 디팟 : 건물, 1개 건물 = 8 유닛.

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("새로운 게임을 시작합니다.")
def game_over():
    pass

game_start()
game_over()
# 다음과 같이 함수 코드를 건너뛰도록 도와준다 : "pass"

class BuildingUnit1(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        #이렇게 하면 상위 클래스의 생성자를 생성한다. 위의 코드와는 비슷하다. 하지만 다중상속을 하게 된다면?
        self.location = location


class Unit1:
    def __init__(self):
        print("유닛1 생성자")

class Flyable1:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit1:
    def __init__(self):
        super().__init__()
        # 다중상속 클래스에서 다음과 같이 수퍼 메소드를 호출하면 가장 마지막 위치한 상속 클래스 생성자가 호출된다.
        # 그래서 다중상속에서는 클래스 명칭을 직접적으로 명시해서 초기화를 해야 한다.


dropship = FlyableUnit1()

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5) 

    #스팀팩을 구현한다.
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("스팀팩을 사용했습니다.")
        else:
            print("체력이 부족합니다.")
    
class Tank(AttackUnit):

    seize_developed = False # 이 친구는 타입 프로퍼티이다. 고유한 값으로 모든 객체에 일괄적으로 적용될 것이다.

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 5)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            print("시즈모드를 업그레이드 해주십시오.")
            return
        
        if self.seize_mode == False:
            print("시즈모드를 전환합니다.")
            self.damage *= 2
            self.seize_mode = True
        else:
            self.damage /= 2
            self.seize_mode = False

def game_start():
    print("게임이 시작되었습니다.")

def game_over():
    print("게임이 끝났습니다.")


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()
m4 = Marine()
t1 = Tank()
t2 = Tank()
t3 = Tank()

attack_units = []

attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(m4)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(t3)

# 모든 유닛 1시로 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발

Tank.seize_developed = True
print("시즈모드 개발이 완료되었습니다.")
# 클래스 자체 인스턴스를 생성하지 않고, 다음과 같이 클래스 자체 전역변수 선언시, 타입 프로퍼티처럼 접근이 가능하다.

# 공격모드 준비(탱크 : 시즈모드, 탱크 : 시즈모드, 레이스 : 클로킹)

for unit in attack_units:
    if isinstance(unit, Marine):
        # isinstance를 통해서 클래스의 인스턴스를 비교 확인한다. 부울 값을 나타낸다. " 지금 유닛이 마린 클래스니?"
        unit.stimpack()# 마린 클래스면 유닛에다가 스팀팩쓴다.
    elif isinstance(unit, Tank):
        unit.set_seize_mode()# 탱크 클래스면 시즈모드 한다.

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))# 해당 범위내에서 일반적인 공격을 받는다.

game_over()

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

    
houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억",  "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)
    

print("총 {0} 대의 매물이 있습니다.".format(len(houses)))

for house in houses:
    house.show_detail()