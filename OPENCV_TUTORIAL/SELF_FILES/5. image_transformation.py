import cv2
import numpy as np 

img = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/group 1.jpg")
cv2.imshow('img', img)

# translate

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    # 다음처럼 넘파이 2차원 배열로 이미지의 이동 좌표를 명시해주어야 한다.
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

# x ==> right, y ==> down

translated_img = translate(img, 10, 20)
cv2.imshow('translated', translated_img)

# Rotation

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimemsions = (width, height)
    
    return cv2.warpAffine(img, rotMat, dimemsions)

rotated_img = rotate(img, 45)
cv2.imshow('rotated', rotated_img)

# resize
resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('resized', resized)

#flip

flip = cv2.flip(img, 0)
# 상하반전 = 0, 좌우반전 = 1, 상하좌우 모두 반전 = -1
cv2.imshow('flip', flip)

cv2.waitKey(0)