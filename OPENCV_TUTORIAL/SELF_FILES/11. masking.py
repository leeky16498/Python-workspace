import cv2 
import numpy as np

img = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/cats.jpg")
cv2.imshow('img', img)

blank = np.zeros((img.shape[:2]), dtype='uint8')
cv2.imshow('blank', blank)

mask = cv2.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv2.imshow('mask', mask)

masked_img = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('masked_img', masked_img)
#마스킹 영역을 설정한 뒤 마스킹으로 이미지를 찍어낼 수 있다.

mask1 = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
masked_new = cv2.bitwise_and(img, img, mask=mask1)
cv2.imshow('mask_rec', masked_new)

weird_mask = cv2.bitwise_and(mask, mask1)
cv2.imshow('weird', weird_mask)

cv2.waitKey(0)