import numpy as np 
import cv2 

haar_cascade = cv2.CascadeClassifier('/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/haarcascades/haarcascade_frontalface_default.xml')

people = ["Ben Afflek", 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy', allow_pickle = True)
# labels = np.load('labels.npy', allow_pickle = True)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('/Users/kyungyunlee/Desktop/face_trained.yml')

img = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/OPENCV_TUTORIAL/opencv-course-master/Resources/Faces/val/ben_afflek/1.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('person', gray)

# detect the face
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    label, confidence = face_recognizer.predict(faces_roi)
    print("label = {}, confidence = {}".format(label, confidence))
    
    cv2.putText(img, str(people[label]), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('detected face', img)
cv2.waitKey(0)