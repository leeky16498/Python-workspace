import cv2
import numpy as np 

img = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/cats.jpg")

cv2.imshow('img', img)

blank = np.zeros(img.shape, dtype='uint8')
cv2.imshow('blank', blank)

gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
# cv2.imshow('blur', blur)

# canny = cv2.Canny(blur, 125, 175)
# cv2.imshow('canny', canny)

ret, threshold = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
# 125보다 작으면 무조건 0으로, 125이상이면 무조건 흰색, 255로, 바이너리(2진수)화 한다.
cv2.imshow('thresh', threshold)

# contours, hierarchies = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# contours, hierarchies = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchies = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(len(contours))

cv2.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv2.imshow('contours draw', blank)
#블러를 적용한 이미지 대비하여 일반 이미지의 컨투어가 더 많이 식별된다.
# 컨투어를 찾고, 이 컨투어를 다시 draw메서드로 그려줄 수 있다.

cv2.waitKey(0)