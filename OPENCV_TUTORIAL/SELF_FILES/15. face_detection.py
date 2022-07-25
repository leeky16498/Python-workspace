import cv2

img = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/group 1.jpg")
cv2.imshow('img', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', img)

haar_cascade = cv2.CascadeClassifier('/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/haarcascades/haarcascade_frontalface_default.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
# minNeighbour가 작아질수록 작은 얼굴을 감지하는 센서티브가 높아진다.

print(len(faces_rect))

for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 4)

cv2.imshow("detected", img)

cv2.waitKey(0)