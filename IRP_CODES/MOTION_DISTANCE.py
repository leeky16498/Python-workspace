import cv2
import numpy as np 
import csv 
from datetime import datetime

VIDEO_NAME = "0_piece_ace"
cap = cv2.VideoCapture("/Users/kyungyunlee/Desktop/ IRP reference/Videos/" + VIDEO_NAME + ".h264")
field_name = ["time", "y_value"]

with open('{}.csv'.format(VIDEO_NAME), 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=field_name)
    csv_writer.writeheader()
    
_, prev = cap.read()
_, new = cap.read()                                                                                       
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
		if cv2.contourArea(contors) > 13000:
			(x,y,w,h) = cv2.boundingRect(contors) # 바운드를 찾고 그 요소를 체크한다.
			cv2.putText(prev, "current 'Y' coordinate : {}".format(int(y+h)), (100,100),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
			cv2.circle(prev, (x,y+h), 5, (255,0,0), 10)
   
			with open('{}.csv'.format(VIDEO_NAME), 'a') as csv_file:
				csv_writer = csv.DictWriter(csv_file, fieldnames=field_name)
				
				info = {
					'time' : (now-old).total_seconds() ,
					'y_value' : int(y+h)
				}
				
				csv_writer.writerow(info)
    
	cv2.imshow("Video_vibration", prev)
	prev = new
	_, new = cap.read()

	if cv2.waitKey(1) == 27: ## esc키를 누르면 프로그램을 종료한다.
		break

cap.release()
cv2.destroyAllWindows()
