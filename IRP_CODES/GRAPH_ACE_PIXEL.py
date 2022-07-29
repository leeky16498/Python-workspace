import pandas as pd 
import matplotlib.pyplot as plt

VIDEO_NAME = "4_piece"

ace_data = pd.read_csv("/Users/kyungyunlee/Desktop/ IRP reference/Data/ACE_DATA/{}.csv".format(VIDEO_NAME))
pixel_data = pd.read_csv("/Users/kyungyunlee/Desktop/ IRP reference/Data/PIXEL_DATA/{}.csv".format(VIDEO_NAME))

plt.subplot(1, 2, 1)
plt.plot(ace_data["time"], ace_data["V"])
plt.grid()
plt.xlim(left=3, right=12)
plt.ylim((-0.3, 0.3))
plt.title("Accelerometer Data")

plt.subplot(1, 2, 2)
plt.plot(pixel_data["time"], pixel_data["y_value"].round(2))
plt.grid()
plt.xlim(left=3.7, right=10)
plt.title("Video Analyzing Data")
plt.show()