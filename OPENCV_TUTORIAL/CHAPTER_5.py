#warp perspective : 이미지중 일부를 잘라서, 매트릭스에 따라 적용하여 보여준다.
import cv2
import numpy as np 
img = cv2.imread("/Users/kyungyunlee/Desktop/PYTHON/OPENCV_TUTORIAL/dog.png")

width, height = 100, 120
pts1 = np.float32([[111, 119], [100, 188], [154, 184], [152, 140]])#그림의 가로세로 꼭지점 좌표.
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_output = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("output", img_output)
cv2.waitKey(0)