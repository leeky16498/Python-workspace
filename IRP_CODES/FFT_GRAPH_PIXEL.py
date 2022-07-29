import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import pandas as pd 

VIDEO_NAME = "40piece"
TIME_1 = 6
TIME_2 = 16
RANK = -2

data = pd.read_csv("/Users/kyungyunlee/Desktop/" + VIDEO_NAME + ".csv")

t = data["time"].loc[data["time"] > TIME_1].loc[data["time"] < TIME_2]
t = np.array(t)
N = len(t)
s = data["y_value"].loc[data["time"] > TIME_1].loc[data["time"] < TIME_2]

# Number of samplepoints
N = len(s)

# sample spacing
T = (t.max()-t.min()) / len(s)
x = np.linspace(0.0, N*T, N)
yf = scipy.fftpack.fft(s)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

# noise passing
yf[0:1] = 0
yf = 2.0/N * np.abs(yf[:N//2])

max_yf = yf.max()
flat = yf.flatten()
flat.sort()
index = np.argwhere(yf == flat[RANK])
max_xf = xf[index]


# draw a graph
plt.figure(figsize=(10, 7))
plt.suptitle("{} | Freq : {}".format(VIDEO_NAME, max_xf[0][0]), fontsize=16, fontweight="bold")
plt.subplot(1, 2, 1)
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("FFT Graph")
plt.plot(xf, yf)
plt.legend()


plt.vlines(x=max_xf, ymax=max_yf + 2, ymin=0, colors="gray", label="Main_frequency = {}".format(max_xf[0][0]))
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(x, s, color='red')
plt.legend()
plt.xlabel("Time")
plt.ylabel("Amplitude(Pixel)")
plt.title("Data Graph")
plt.show()