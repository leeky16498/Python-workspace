import numpy as np

sticker = [6, 11, 13, 15, 13]

for i in range(len(sticker)):
    if i % 2 == 0:
        del sticker[i]
        
print(sticker)