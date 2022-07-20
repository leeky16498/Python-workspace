import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

data = pd.read_csv("/Users/kyungyunlee/Desktop/ IRP reference/Data/PIXEL_DATA/1_piece.csv")

t = data["time"].loc[data["time"] > 5].loc[data["time"] < 10]
N = len(t)
s = data["y_value"].loc[data["time"] > 5].loc[data["time"] < 10]
s = np.array(s)

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.array(t)
y = np.array(s)
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show()