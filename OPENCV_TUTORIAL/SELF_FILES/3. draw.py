import cv2
import numpy as np 

blank = np.zeros((500, 500, 3), dtype='uint8')
cv2.imshow('blank', blank)
# img = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/cat.jpg")
# cv2.imshow('cat', img)

#1. paint the image a certain color
blank[:] = 0, 255, 0
cv2.imshow('green', blank)

blank[200:300, 300:400] = 0, 0, 255
cv2.imshow('partial', blank)

#2. draw rectangle
# cv2.rectangle(blank, (100, 100), (200, 200), (255, 0, 0), -1)
cv2.rectangle(blank, (100, 100), (blank.shape[0], blank.shape[1]), (255, 0, 0), -1)
# 다음처럼 길이 제공 시 shape프로퍼티를 통해서 직접 정확하게 접근하는 방법도 있다.
# source image, pt1, pt2, color, thickness // if -1? filled rectangle
cv2.imshow('rectangle', blank)

#3. draw circle
cv2.circle(blank, (250, 250), 20, (250, 250, 0), -1)
# source image, radius, color, thickness // if -1? filled circle
cv2.imshow('circle', blank)

#4. draw line
cv2.line(blank, (0, 0,), (250, 250), (0, 255, 0), 3)
# source image, pt1, pt2, color, thickness
cv2.imshow('line', blank)

#5. write text
cv2.putText(blank, 'hello', (225, 225), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
# image, text, coordinates, font, fontscale, color
cv2.imshow('text', blank)
cv2.waitKey(0)
# 키의 입력을 기다리며, 하나라도 눌리면 루프를 종료한다.