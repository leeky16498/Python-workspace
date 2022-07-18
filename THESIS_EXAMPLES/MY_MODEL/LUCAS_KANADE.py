import cv2
from cv2 import EVENT_LBUTTONDOWN
import numpy as np 
import csv
import time
from itertools import count
from datetime import datetime, timedelta
from GRAPH_PLOTTER import DrawGraph

cap = cv2.VideoCapture('/Users/kyungyunlee/Desktop/PYTHON_FOLDER/THESIS_EXAMPLES/MY_MODEL/Video_0.h264')
field_name = ["x_value", "y_value"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=field_name)
    csv_writer.writeheader()

_, frame = cap.read()
old_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

lk_params =  dict(winSize = (10, 10),
                  maxLevel = 2, 
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

def select_point(event, x, y, flags, params):
    global point, point_selected, old_points
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x, y)
        point_selected = True
        old_points = np.array([[x, y]], dtype="float32")
        
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", select_point)

point_selected = False
point = ()
old_points = np.array([[]])
old = datetime.now()

while True:

    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if point_selected:
        now = datetime.now()
        cv2.circle(frame, point, 5, (0, 0, 255), 5)
        new_points, status, error = cv2.calcOpticalFlowPyrLK(old_gray,
                                                             gray_frame,
                                                             old_points,
                                                             None,
                                                             **lk_params)
        old_gray = gray_frame.copy()
        old_points = new_points 
        x, y = new_points.ravel()
        print(new_points)
        cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 0), -1)
        
        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=field_name)
            
            info = {
                'x_value' : (now-old).total_seconds() ,
                'y_value' : int(point[1] - int(y))
            }
            
            csv_writer.writerow(info)
    
    cv2.imshow("Frame", frame)
  
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
graph = DrawGraph()