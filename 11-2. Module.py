### 모듈 개념 ###

## 모듈이라 함은 일반적으로 사용 목적을 지닌 코드들의 묶음이라고 생각하면 된다.
## 다음처럼 모듈 안에는 다양한 함수가 구현되어 있다.

#일반 가격

def price(people):
    print("{0} 명 가격은 {1} 입니다.".format(people, people*10000))

#조조할인

def price_morning(people):
    print("{0} 명 가격은 {1} 입니다.".format(people, people*6000))

#군인할인

def price_soldier(soldiers):
    print("{0} 명 가격은 {1} 입니다.".format(soldiers, soldiers*4000))

# 모듈은 같은 파일 경로내에서만 소통이 가능하다.
