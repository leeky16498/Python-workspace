import os
import numpy as np
from numpy.fft import fft2, ifft2
from scipy.signal import gaussian, convolve2d
import matplotlib.pyplot as plt
import cv2

def wiener_filter(img, kernel, K):
	kernel /= np.sum(kernel)
	dummy = np.copy(img)
	dummy = fft2(dummy)
	kernel = fft2(kernel, s = img.shape)
	kernel = np.conj(kernel) / (np.abs(kernel) ** 2 + K)
	dummy = dummy * kernel
	dummy = np.abs(ifft2(dummy))
	return dummy

def gaussian_kernel(kernel_size = 3):
	h = gaussian(kernel_size, kernel_size / 3).reshape(kernel_size, 1)
	h = np.dot(h, h.transpose())
	h /= np.sum(h)
	return h

def rgb2gray(rgb):
	return np.dot(rgb[...,:3], [1, 1, 1])

img = cv2.imread()

# if __name__ == '__main__':
# 	# Load image and convert it to gray scale
# 	file_name = os.path.join('/Users/kyungyunlee/Desktop/PYTHON_FOLDER/THESIS_EXAMPLES/MY_MODEL/Frame_image/0piece_middle0.jpg') 
    
# 	img = rgb2gray(plt.imread(file_name));cv2.imshow(img)

# 	# Apply Wiener Filter
# 	kernel = gaussian_kernel(10)
# 	filtered_img = wiener_filter(img, kernel, K = 10)

# 	# Display results
# 	display = [img, filtered_img]
# 	label = ['Original Image','Wiener Filter applied']

# 	fig = plt.figure(figsize=(12, 10))

# 	for i in range(len(display)):
# 		fig.add_subplot(1, 2, i+1)
# 		plt.imshow(display[i])
# 		plt.title(label[i])

# 	plt.show()