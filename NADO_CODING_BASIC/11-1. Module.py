### 모듈 사용의 예시이다.

# import theater_module

# theater_module.price(3) # 3명이서 영화보러 가면?
# theater_module.price_morning(3)# 3명 조조할인 가격?

# 다음처럼 import를 통해서 모듈간의 소통이 가능하다.

# import theater_module as mv # as뒤에 붙여주면 별명을 지어줄 수 있다.

# mv.price(3)
# mv.price_morning(3)
# mv.price_soldier(3)

# 모듈명을 다음처럼 축약가능하다.

# from theater_module import *
# price(3)
# price_morning(3)
# price_soldier(3)

# from을 써주게 되면 바로바로 그냥 . 없이 바로 사용 가능하다.

# from theater_module import price, price_morning
# price(5)
# price_morning(5)
# price_soldier(7)
# 우측에 쓰기로 한 함수로 정의하지 않았으므로 인식을 못한다.

# 쓸 함수 자체에 대해서도 별명을 지어서 편하게 쓸 수 있다.
from theater_module import price_soldier as ps
ps(3)