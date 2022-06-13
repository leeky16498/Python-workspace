##opencv의 좌표평면, 좌상단이 0 지점이다.
import cv2
import numpy as np

img = cv2.imread("/Users/kyungyunlee/Desktop/PYTHON/OPENCV_TUTORIAL/dog.png")
print(img.shape)
cv2.imshow("Image", img)

img_resize = cv2.resize(img, (100, 150)) #가로세로 길이 조절이 가능해진다.# 하지만 여기는 가로 먼저 세로 이후
print(img_resize.shape)
cv2.imshow("Resize", img_resize)##사이즈 조절이 가능하다.

img_cropped = img[0:200, 200:500]# 높이 먼저, 가로 이후
cv2.imshow("cropped", img_cropped) #이미지 잘라내기