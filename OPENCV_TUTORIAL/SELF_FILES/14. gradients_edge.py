import cv2 
import numpy as np 

img = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/cats.jpg")
cv2.imshow("img", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

#laplacial : 라플라시안 엣지 디텍터
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('lap', lap)

#sobel : 소블 그래디언트 컴퓨팅
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
combine_sobel = cv2.bitwise_or(sobelx, sobely)
cv2.imshow('sobelx', sobelx)
cv2.imshow('sobely', sobely)
cv2.imshow('combine', combine_sobel)
# 엑스방향과 와이방향 측의 두께를 측정하는 형태로 이미지의 엣지를 분석하는 것이다.

# 가장 유명한 엣지 디텍터 중 하나인 캐니 디텍터
canny = cv2.Canny(gray, 150, 175)
cv2.imshow('canny', canny)

cv2.waitKey(0)