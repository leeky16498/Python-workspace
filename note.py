# 1. 0이상의 정수를 입력받기
NUM_RIGHT = False

while not NUM_RIGHT:
    num = int(input("Give me the number higher than 5"))
    print(num)
    if num < 5:
        print('number is smaller than 5')
    else:
        print("good number")
        NUM_RIGHT = True
        
print(num)

#2. 타율 구하기
HIT = int(input('How many the batter hit the ball?'))
NUMBER = int(input('How many the batter did try?'))

def pct_hit(numbers, hit):
    PCT = (HIT) / (NUMBER)
    print(round(PCT, 3))

pct_hit(NUMBER, HIT)
