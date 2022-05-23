# 마린 : 공격유닛, 군인. 총을 쏠 수 있다.

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
class Unit:
    def __init__(self, name, hp, damage, speed):# 파이썬에서는 self 파라미터도 전부 같이 넘겨주어야 한다.
        # 이 친구는 생성자 호출부분이다. 클래스 인스턴스를 생성할 때 호출이 되는 부분이다.
        self.name = name
        self.hp = hp
        self.damage = damage
        self.speed = speed

    def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
            .format(self.name, location, self.speed))

    
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


## 메소드에 대해서 알아본다.

# 클래스 옆에 ()안에 클래스 이름을 넣으면 해당 클래스를 상속받는다.
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, damage, speed)# 슈퍼 클래스 생성자를 받아온다.
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

#발키리를 제작해본다.

valkirie1 = FlyableAttackUnit("발키리1", 250, 15, 5)
valkirie1.fly(valkirie1.name, "3시")

# 연산자 오버라이딩에 대해서 알아본다. 쉽게 말하면 상속받는 것들을 재정의하는 것이라고 보면 된다.

vulture = AttackUnit("벌쳐", 80, 10, 10)
vulture.move("11시")

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
battlecruiser.move("9시")