##이미지 조인하기.
import cv2
import numpy as np 

img = cv2.imread("/Users/kyungyunlee/Desktop/PYTHON/OPENCV_TUTORIAL/dog.png")
# img_hor = np.hstack((img, img))
# #이미지를 ㅁㅁ 이렇게 평행하게 붙인다.

# img_ver = np.vstack((img, img))
# #이미지를 세로로 평행하게 붙인다.

# cv2.imshow("horizontal-image", img_hor)
# cv2.imshow("vertica_image", img_ver)

cv2.waitKey(0)