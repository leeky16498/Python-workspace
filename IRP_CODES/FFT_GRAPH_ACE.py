import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import pandas as pd 

VIDEO_NAME = "40_piece_ace"
TIME_1 = 6.2
TIME_2 = 26
RANK = -1

data = pd.read_csv("/Users/kyungyunlee/Desktop/ IRP reference/Data/ACE_DATA/" + VIDEO_NAME + ".csv")

t = data["time"].loc[data["time"] > TIME_1].loc[data["time"] < TIME_2]
t = np.array(t)
print(t)
N = len(t)
s = data["V"].loc[data["time"] > TIME_1].loc[data["time"] < TIME_2]
s = np.array(s)
print(s)

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
# index = np.argwhere(yf == max_yf)
max_xf = xf[index]


# draw_the graph
plt.figure(figsize=(10, 7))
plt.suptitle("{}".format(VIDEO_NAME), fontsize=16, fontweight="bold")
plt.subplot(1, 2, 1)
plt.xlabel("Frequency")
plt.xlim(0, 20)
plt.ylabel("Amplitude")
plt.title(f"FFT : {max_xf[0][0]}")
plt.plot(xf, yf)


# plt.vlines(x=max_xf, ymax=max_yf + 2, ymin=0, colors="gray", label="Main_frequency = {}".format(max_xf[0][0]))
plt.subplot(1, 2, 2)
plt.plot(x, s, color='red')
# plt.legend()
plt.xlabel("Time")
plt.ylabel("Amplitude(Pixel)")
plt.title("Data Graph")
plt.show()