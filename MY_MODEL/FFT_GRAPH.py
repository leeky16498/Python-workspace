import numpy as np  
import matplotlib.pyplot as plt 
import pandas as pd 
plt.style.use("seaborn")

df = pd.read_csv("PYTHON_FOLDER/data.csv")
t = df["time"].loc[df["time"] > 0.5].to_list()
t = np.array(t)

signal = df["y_value"].loc[df["time"] > 0.5].to_list()
signal = np.array(signal)

strength = np.fft.fft(signal)
strength = abs(strength)
frequency = np.fft.fftfreq(t.size, 0.001)


plt.subplot(1, 2, 1)
plt.plot(t, signal)
plt.subplot(1, 2, 2)
plt.plot(frequency, strength)
plt.xlim(0, 100)
plt.show()
