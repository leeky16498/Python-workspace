import cv2 
import matplotlib.pyplot as plt
import numpy as np

# img = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/cats.jpg")
img = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/cats 2.jpg")
cv2.imshow("img", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask_img = cv2.bitwise_and(gray, gray, mask=mask)
cv2.imshow('mask_img', mask_img)

#g_scale hist
# gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
gray_hist = cv2.calcHist([gray], [0], mask,[256], [0, 256])

# plt.figure()
# plt.title("gray_hist")
# plt.xlabel("Bins")
# plt.ylabel("num of pixels")
# plt.plot(gray_hist)
# plt.show()
# 기본적으로 밝은 이미지, 하얀색에 가까운 이미지가 높은 값을 가지게 된다.

# colours Histogram
plt.figure()
plt.title("gray_hist")
plt.xlabel("Bins")
plt.ylabel("num of pixels")
    
colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv2.waitKey(0)