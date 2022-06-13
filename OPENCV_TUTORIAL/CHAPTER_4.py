##shape and texts
import cv2
import numpy as np

# img = np.zeros((512, 512))
img = np.zeros((512, 512,3), np.uint8)
print(img)
##까만화면을 나타낸다.

# img[:] = 255,0,0
img[200:300, 100:300] = 255,0,0

#부분 색상 지정 가능

# cv2.line(img,(0,0),(300, 300), (0, 255, 0)) #양 쪽 끝점 좌표, 선 색상
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0)) #이미지의 대각 양 끝을 지정가능하다.
# cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255), 5) #가장 마지막은 두께다
cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255), cv2.FILLED) #직사각형의 넓이가 꽉 차있음.
cv2.circle(img, (400, 50), 30, (255, 255, 0), 3) #순서대로 원점좌표, 지름, 원주색상, 두께
cv2.putText(img, 
            "This is opencv class", (200, 200), 
            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
# 이미지, 텍스트, 좌표, 폰트(스케일, 색, 두께)


cv2.imshow("window", img)
cv2.waitKey(0)