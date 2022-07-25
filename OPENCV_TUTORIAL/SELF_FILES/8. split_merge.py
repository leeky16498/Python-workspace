import cv2 
import numpy as np 


img = cv2.imread('/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/cats 2.jpg')
print(img.shape)
blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv2.split(img)
print(b, g, r)

cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)
cv2.imshow('img', img)
# 이 상태에서는 흑백 이미지만 나오게 된다.

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

blue = cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])
# 흑백 계열 행렬을 더해서 만들어주면, 본연의 색을 찾게 된다.

cv2.imshow('mer_red', red)

cv2.waitKey(0)