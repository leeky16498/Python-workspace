# 이미지 질감 수정
import numpy as np
import cv2

img = cv2.imread(filename="/Users/kyungyunlee/Desktop/PYTHON/OPENCV_TUTORIAL/dog.png")
kernel = np.ones((5, 5), np.uint8) # 이미지의 차원을 지정해주는 것이다.

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#회색이미지로 설정
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)#블러 이미지 설정
img_canny = cv2.Canny(img, 150, 200) #높게나 낮게 설정 가능하다. 높아질수록 테두리가 덜생긴다.
img_dialation = cv2.dilate(img_canny, kernel, iterations=1)
img_eroded = cv2.erode(img_dialation, kernel, iterations=1)

cv2.imshow("Gray Image", img_gray)
cv2.imshow("blur image", img_blur) # 블러이미지를 생성
cv2.imshow("Canny image", img_canny) # edge이미지 생성
cv2.imshow("dialation image", img_dialation) # edge이미지 테두리 두께 설정
cv2.imshow("erosion", img_eroded)
cv2.waitKey(0)


## 엣지 디텍터, cannyedgedetector
