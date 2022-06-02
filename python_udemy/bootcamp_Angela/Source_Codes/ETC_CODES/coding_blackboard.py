from hashlib import new
import math
import random

from numpy import short

list = [1, 2, 3]
list2 = [item+1 for item in list] #맵이랑 비슷하다.
print(list2)
## 리스트 컴프리헨션
## 리스트에서는 조건이 포함된 컴프리헨션이 가능하다.

# new_list = [new_item for item in list if test]
## if 구문을 통해서 조건문을 집어넣는 것이 가능하다.

names = ["alex", "beth", "Dave", "Elanor", "Freddie", "Joe", "Kayle"]

short_names = [name.upper() for name in names if len(names) > 3]
print(short_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

new_numbers = [num**2 for num in numbers]
print(new_numbers)
## **을 통해서 다음과 같이 제곱 시행이 가능하다.
even_nums = [nums for nums in new_numbers if nums % 2 == 0]
print(even_nums)
## 짝수를 걸런내는 경우


## 딕셔너리 컴프리헨션 적용하기

# new_dict = {new key:new value for (key, value) in dict.items() if test} 똑같은 룰에 따라서 적용된다.

student_score = {
    "Alex" : 80,
    "Kayle" : 90,
    "Garen" : 100
}

new_dict = {key:value for (key, value) in student_score.items() if key == "Garen"}
print(new_dict)

import pandas as pd

student_dict1 = {
    "student" : ["Lee", "Kin", "Park"],
    "score" : [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_dict1)
print(student_data_frame)
## 판다스에서도 똑같이 컴프리핸션이 가능하다.

for (key, value) in student_data_frame.items():
    print(value)
    
for (index, row) in student_data_frame.iterrows():
    print(index)
    
for (index, row) in student_data_frame.iterrows():
    print(row)
    print(row.student)
    print(row.score)## 데이터 값 조회가 가능한 것을 보고 계십니다.
##판다스에서는 iterrow메서드를 통해서 각 row별 데이터 출력이 가능하다.