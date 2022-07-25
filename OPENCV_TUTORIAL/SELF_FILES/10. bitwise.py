import cv2 
import numpy as np 

img = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/cat.jpg")
cv2.imshow('img', img)

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv2.circle(blank.copy(), (200, 200), 200, 255, -1)

cv2.imshow("rec", rectangle)
cv2.imshow('circle', circle)

# 1. bitwise_and : 두 이미지 간에 모두 255로 하얀색이 겹치는 부분을 잘라낸다.
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow('bitwise_and', bitwise_and)

# 2. bitwise_or : 두 이미지간에 하나라도 흰색인 부분을 모두 합쳐서 다시 그려내준다.
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow('bitwise_or', bitwise_or)

# 3. bitwise_xor : 겹치는 부분은 0으로 안겹치는 부분은 하얗게 처리를 해준다.
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('bitwise_xor', bitwise_xor)

# 4. bitwise_not : 도형의 형태에 대해서 완전히 반전을 주게 된다.
bitwise_not = cv2.bitwise_not(rectangle)
cv2.imshow('bitwise_not', bitwise_not)

cv2.waitKey(0)