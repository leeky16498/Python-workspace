# 이미지를 읽어오고, 웹캠 작동시키기
import numpy as np
import cv2

img = cv2.imread(filename="/Users/kyungyunlee/Desktop/PYTHON/OPENCV_TUTORIAL/dog.png")
kernel = np.ones((5, 5), np.uint8)
cv2.imshow("Output", img)
cv2.waitKey(0)
# 이미지를 띄운다.
# ms단위이다.

cap = cv2.VideoCapture("/Users/kyungyunlee/Desktop/PYTHON/OPENCV_TUTORIAL/file.mp4")
cap.set(3, 640)
cap.set(4, 480)
# 비디오 화면의 가로세로를 정해줄 수 있다.
cap.set(10, 100)
# 셋 앞의 숫자가 가로, 세로, 배경을 정해주는 키 값으로 판단된다.

#연속된 사진의 구성이기 때문에, 아래처럼 무한 반복으로 비디오를 재생해준다.
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    # ""는 타이틀이 들어간다.
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # 키 q를 누르면 이미지를 종료한다.