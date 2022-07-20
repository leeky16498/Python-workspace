import numpy as np 
from scipy import fftpack 
import matplotlib.pyplot as plt 
plt.style.use("seaborn")

time_step = 0.05
time_vec = np.arange(0, 10, time_step)
period = 5

sig = (np.sin(2*np.pi*time_vec/period)+0.25*(np.random.randn(time_vec.size)))
print(np.round(sig, 3)) # 뒤에 렌덤 노이즈를 발생시켜준다.

sig_fft = fftpack.fft(sig)
amplitude = np.abs(sig_fft)
power = amplitude ** 2
angle = np.angle(sig_fft)

sample_freq = fftpack.fftfreq(sig.size, d=time_step)
print(sample_freq)
amp_freq = np.array([amplitude, sample_freq])
amp_position = amp_freq[0,:].argmax()  
peak_freq = amp_freq[1, amp_position]

print(amp_position)
print(peak_freq)

high_freq_fft = sig_fft.copy()
high_freq_fft[np.abs(sample_freq) > peak_freq] = 0

filtered_sig = fftpack.ifft(high_freq_fft)

plt.plot(time_vec, filtered_sig)
plt.plot(time_vec, sig)
plt.show()

