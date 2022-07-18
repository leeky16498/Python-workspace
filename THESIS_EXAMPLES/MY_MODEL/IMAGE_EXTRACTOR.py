import cv2 
import numpy as np 

cap = cv2.VideoCapture("/Users/kyungyunlee/Desktop/PYTHON_FOLDER/THESIS_EXAMPLES/MY_MODEL/0piece_middle.h264")

i = 0

while(cap.isOpened()):
    suc, frame = cap.read()
    if suc == False:
        break
    path = "/Users/kyungyunlee/Desktop/PYTHON_FOLDER/THESIS_EXAMPLES/MY_MODEL/Frame_image/0piece_middle" + str(i) + '.jpg'
    cv2.imwrite(path, frame)
    i += 1
    
cap.release()
cv2.destroyAllWindows()