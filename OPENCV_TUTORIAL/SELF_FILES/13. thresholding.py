import cv2 

# thresholding ? 이미지를 2진화해주는 것이다. 검정과 하얗 두개로만.
img = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/cats.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# simple thresholding
threshold, thresh = cv2. threshold(gray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh', thresh)

# simple thresholding inverse
threshold_inv, thresh_inv = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('thresh_inv', thresh_inv)

# adaptive thresholding
# thresh_adap = cv2.threshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
# cv2.imshow('thresh_adap', thresh_adap)
# 여기는 다시 확인해보고 적용하기


cv2.imshow("img", img)
cv2.waitKey(0)