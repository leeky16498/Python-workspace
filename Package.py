# from travel import vietnam
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# # 주의할 점으로 임포트 할때는 모듈이나 패키지만 가능하다. 나머지는 import 가 불가능하다.
# # 패키지는 일종의 코드 모듈들을 모아 둔 폴더를 의미하며, import를 통해 사용 가능하다.

# from travel.vietnam import VietnamPackage
# trip_t0 = VietnamPackage()
# trip_t0.detail()

# 다음처럼 from, import를 통해서도 자연스럽게 사용이 가능하다.



##__all__에 대해서 알아본다.
from travel import * 
trip_to2 = vietnam.VietnamPackage()
trip_to2.detail()

# 생성자.py에서 all에 대한 리턴 모듈을 지정해주니 오류가 나지 않는다.
# 여기에서 처럼 *를 활용해서 모듈 내 모든 기능을 가져온다고 하면 오류가 난다. 그래서 별도의 생성자 모듈을 통해서 가져온다.

import inspect
import random

print(inspect.getfile(random))
print(inspect.getfile(thailand))

# 임폴트 된 각 모듈의 경로를 터미널에 나타내준다.