import pandas as pd 
import matplotlib.pyplot as plt

VIDEO_NAME = "5_piece_ace"

ace_data = pd.read_csv("/Users/kyungyunlee/Desktop/ IRP reference/Data/ACE_DATA/{}.csv".format(VIDEO_NAME))
pixel_data = pd.read_csv("/Users/kyungyunlee/Desktop/ IRP reference/Data/PIXEL_DATA/{}.csv".format(VIDEO_NAME))

plt.figure(figsize=(12, 9))
plt.subplot(1, 2, 1)
plt.plot(ace_data["time"], ace_data["V"])
plt.xlim(left=0, right=50)
plt.xlabel("time")
plt.ylabel("V")
plt.ylim((-0.3, 0.3))
plt.title("Accelerometer Data")

plt.subplot(1, 2, 2)
plt.plot(pixel_data["time"], pixel_data["y_value"].round(2))
plt.xlim(left=0, right=50)
plt.xlabel("time")
plt.ylabel("pixel_y")
plt.title("Video Analyzing Data")
plt.show()