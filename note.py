import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import pandas as pd 


data = pd.read_csv("/Users/kyungyunlee/Desktop/ IRP reference/Data/PIXEL_DATA/20_piece.csv")

t = data["time"].loc[data["time"] > 5].loc[data["time"] < 10]
t = np.array(t)
print(t)
N = len(t)
s = data["y_value"].loc[data["time"] > 5].loc[data["time"] < 10]
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

plt.figure(figsize=(10, 7))

plt.subplot(1, 2, 1)
plt.xlabel("Frquency")
plt.ylabel("Amplitude")
plt.title("FFT Graph")
plt.plot(xf, yf)

max_yf = yf.max()
index = np.argwhere(yf == max_yf)
max_xf = xf[index]

plt.vlines(x=max_xf, ymax=yf.max() + 2, ymin=0, colors="gray", label="Main_frequency = {}".format(max_xf[0][0]))
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(x, s, color='red')
plt.xlabel("Pixel Amplitude")
plt.ylabel("Time")
plt.title("Data Graph")
plt.show()