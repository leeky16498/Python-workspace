import os 
import caer
import canaro
import numpy as np 
import cv2 
import gc

IMG_SIZE = (80, 80)
channels = 1
# grayscale = 1

char_path = "Simpson_data/simpsons_dataset"

char_dict = {}

for char in os.listdir(char_path):
    char_dict[char] = len(os.listdir(os.path.join(char_path, char)))
    
# sort in descending order

char_dict = caer.sort_dict(char_dict, descending=True)
print(char_dict)