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
