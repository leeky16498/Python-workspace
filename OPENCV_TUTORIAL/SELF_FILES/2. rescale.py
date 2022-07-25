import cv2

img = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Photos/cat.jpg")
# cv2.imshow("cat", img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    
    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)

def changeResolution(width, height):
    # 이것은 온리 웹캠에 대해서만, 라이브 비디오 대해서만 적용된다.
    # set메서드를 통해서 가로, 세로의 비율을 정해줄 수 있는 것이다.
    cap.set(3, width)
    cap.set(4, height)

# 다음 함수를 통해서 0.75 작아진 이미지와 비디오를 불러올 수 있다.
resized_image = rescaleFrame(img)
cv2.imshow("image", resized_image)

cap = cv2.VideoCapture("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Videos/dog.mp4")
# 이미지 불러올때는 imread로 하고,
# 비디오를 불러올때는 VideoCapture로 한다.

while True:
    isTrue, frame = cap.read()
    frame_resized = rescaleFrame(frame)
    
    cv2.imshow('video', frame)
    cv2.imshow('resized', frame_resized)
    
    if cv2.waitKey(20) & 0xFF == ord("d"):
        break

cap.release()
cv2.destroyAllWindows()