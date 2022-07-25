import cv2

img = cv2.imread("Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/cat.jpg")
cv2.imshow('img', img)

# 1. averaging
average = cv2.blur(img, (3, 3))
# average = cv2.blur(img, (7, 7))
# 커널사이즈가 커질수록 블러도 심해진다.
cv2.imshow('average', average)

# 2. Gaussian Blur : more natural than average
gauss = cv2.GaussianBlur(img, (3, 3), 0)
cv2.imshow('gauss', gauss)

# 3. Median Blur : average는 평균을 찾지만, median은 중간값으로 찾아간다.
median = cv2.medianBlur(img, 7)
# 여기에서는 별도의 커널 사이즈를 2차원으로 넘기지 않는다.
cv2.imshow('median', median)

# 4. Bilateral
# 블러를 먹이지만 이미지의 경계선을 살리는 블러링
bilateral = cv2.bilateralFilter(img, 5, 35, 25)
# 이미지, 커널사이즈, 시그마컬러(색은 35 픽셀 주변으로 고려), 시그마 스페이스(고려하는 영역을 25로 수정)
cv2.imshow('bilateral', bilateral)

cv2.waitKey(0)