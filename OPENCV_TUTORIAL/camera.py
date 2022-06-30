import cv2

face_detector = cv2.CascadeClassifier("/Users/kyungyunlee/Desktop/PYTHON/OPENCV_TUTORIAL/Images/haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0) # 넘버 0는 웹켐을 의미, 1은 다른 카메라

while True:
    ret, frame = video_capture.read()
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detections = face_detector.detectMultiScale(image_gray, minSize = (100, 100))
    
    for (x, y, w, h) in detections:
        print(w, h)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow('video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break