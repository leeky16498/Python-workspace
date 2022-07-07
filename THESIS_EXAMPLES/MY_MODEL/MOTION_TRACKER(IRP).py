import cv2
import numpy as np 
import csv 
from datetime import datetime
from GRAPH_PLOTTER import DrawGraph

cap = cv2.VideoCapture('/Users/kyungyunlee/Desktop/PYTHON/THESIS_EXAMPLES/MY_MODEL/TEST_VIDEO_5.h264')
field_name = ["x_value", "y_value"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=field_name)
    csv_writer.writeheader()
    
_, prev = cap.read()
prev = cv2.flip(prev, 1)
_, new = cap.read()                                                                                       
new = cv2.flip(new, 1)
old = datetime.now()

while True:
	diff = cv2.absdiff(prev, new) # 움직임이 있다면 diff가 0이 아닐 것이며, 움직임이 감지되면 diff가 0이다.
	diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)# 그리고 그 움직임의 차이 픽셀을 회색계열로 변환해주고
	diff = cv2.blur(diff, (5,5))
	_,thresh = cv2.threshold(diff, 10, 255, cv2.THRESH_BINARY) # 그리고 threshold함수를 통해서 thresh 바이너리로 변경해준다.
	thresh = cv2.dilate(thresh, None, 3)
	thresh = cv2.erode(thresh, np.ones((4,4)), 1)
	contor,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	now = datetime.now()
 
	for contors in contor:				
		if cv2.contourArea(contors) > 10000:
			(x,y,w,h) = cv2.boundingRect(contors)
			cv2.putText(prev, "'Y pixel coordinate' : {}".format(int(y)), (100,100),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
			cv2.circle(prev, (x,y), 5, (0,0,255), 10)
   
			with open('data.csv', 'a') as csv_file:
				csv_writer = csv.DictWriter(csv_file, fieldnames=field_name)
				
				info = {
					'x_value' : (now-old).total_seconds() ,
					'y_value' : int(y)
				}
				
				csv_writer.writerow(info)
   
   
	cv2.imshow("orig", prev)
	
	prev = new
	_, new = cap.read()

	if cv2.waitKey(1) == 27:
		break

cap.release()
cv2.destroyAllWindows()
graph = DrawGraph()
graph.draw_frequency()