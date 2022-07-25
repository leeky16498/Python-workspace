import cv2 
import matplotlib.pyplot as plt

img = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/cats.jpg")
# cv2.imshow('img', img)

# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', img_gray)

# # BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)

# BGR to L*A*B
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)

# COLOR BGR to RGB(for plt)
inversed = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(inversed)
# plt.show()
cv2.imshow('inversed', inversed)
# 모두 다 인버스가 가능하지만, Gray -> HSV는 불가능하다.

hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('hsv_bgr', hsv_bgr)

cv2.waitKey(0)