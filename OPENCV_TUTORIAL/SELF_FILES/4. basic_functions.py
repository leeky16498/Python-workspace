import cv2
import numpy as np 

img = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/cats.jpg")
cv2.imshow('cat', img)

# 1. convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('graay', img_gray)
print(img_gray.shape)

#2. blur
blur = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)
blur = cv2.GaussianBlur(img, (7, 7), cv2.BORDER_DEFAULT)
# image, kernelsize(odd), property, 커널 사이즈가 커지면 블러가 더 심하게 생긴다.
cv2.imshow('blur', blur)

#3. edge cascade
canny = cv2.Canny(img, 125, 175)
# 색 지수 125를 기점으로 하여 엣지를 찾아내는 것이다.
cv2.imshow('canny', canny)

#4. dilating the image
dilated = cv2.dilate(canny, (3, 3), iterations=1)
# dilated = cv2.dilate(canny, (7, 7), iterations=7)
cv2.imshow('dilate', dilated)
#팽창을 사용하면, 엣지를 더 선명하게 부각시킨다.
#커널과 이터레이션이 커지면 엣지가 더 두툼하게 팽창된다. 두꼐가 증가하는 거지

#5. erode the image
eroded = cv2.erode(canny, (3, 3), iterations=1)
cv2.imshow('eroded', eroded)
# 침식시키게 되면 얇아지며 정확한 뼈대를 볼 수 있다.

#6. resize
resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_AREA)
# resized = cv2.resize(img, (1000, 1000), interpolation=cv2.INTER_LINEAR)
# 만약 사진을 작게하면 인터 에어리어
# 만약 크게 하면, 인터 리니어나, 인터 큐빅을 쓴다.
# 튜플값만큼 사진 비율을 무시한 가운데 사이즈가 조정된다.
cv2.imshow('resized', resized)

#7. crop
cropped = img[50:100, 40:100]
cv2.imshow('cropped', cropped)
# 이미지 잘라내기

cv2.waitKey(0)