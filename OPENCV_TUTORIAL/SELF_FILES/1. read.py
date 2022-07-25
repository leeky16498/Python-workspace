import cv2

# img = cv2.imread('/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/cat.jpg')
# cv2.imshow("cat_large.jpg", img)
# cv2.waitKey(0)

# 이걸 설정해주면, 키보드가 눌리기 전까지 계속 이미지를 띄운다.
# 이미지를 불러오는 아주 심플한 메서드.
# waitKey(0)를 하게 되면 별도의 키보드를 누르기 전까지 이미지를 계속 띄운다. 

cap = cv2.VideoCapture("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Videos/dog.mp4")
# 0 : 웹캠, 1 : 그 다음 당신이 설정한 카메라 순으로 넘어가게 된다.

while True:
    isTrue, frame = cap.read()
    # video파일.read()를 통해서 비디오를 불러온다. 이 때 각 프레임을 돌리게 될 것이다.
    # 그 프레임 사진 파일은 frame이라는 이미지로 매 순간 루프를 돌며 들어오게 된다.
    # isTrue : 프레임이 잘 제공되고 있는지에 대해 제공한다 불리언 값
    # frame = 프레임은 말그대로 프레임이다.
    
    cv2.imshow("video", frame)
    
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break 
    # 다음과 같이 설정하면 d키를 누르게 되면 비디오를 끄고 나간다. 라는 의미이다.
    # 비디오 프레임이 모두 다 끝나면 -215 에러를 발생시킨다.(더 이상 재생시킬 이미지가 없다는 의미이다.)

cap.release()
cv2.destroyAllWindows()