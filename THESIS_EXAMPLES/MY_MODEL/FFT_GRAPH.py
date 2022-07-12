import numpy as np  
import matplotlib.pyplot as plt 
import pandas as pd 
plt.style.use("seaborn")

df = pd.read_csv("/Users/kyungyunlee/Desktop/PYTHON_FOLDER/data.csv")
t = df["time"].to_list()
t = np.array(t)

signal = df["y_value"].to_list()
signal = np.array(signal)

strength = np.fft.fft(signal)
strength = abs(strength)
frequency = np.fft.fftfreq(t.size, 0.001)

plt.plot(frequency, strength)
plt.xlim(0, 100)
plt.show()
