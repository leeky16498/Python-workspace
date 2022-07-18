import cv2
import os 

path = "/Users/kyungyunlee/Desktop/PYTHON_FOLDER/THESIS_EXAMPLES/MY_MODEL/Frame_image/"
out_path = "/Users/kyungyunlee/Desktop/PYTHON_FOLDER/THESIS_EXAMPLES/MY_MODEL/"
out_video_name = "sample_video.mp4"

out_video_full_path = out_path + out_video_name

pre_imgs = os.listdir(path)
# print(pre_imgs)
img = []
i = 0

for i in range(len(pre_imgs)):
    image = path+"0piece_middle"+str(i)+".jpg"
    img.append(image)

print(img)

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

frame = cv2.imread(img[0])
size = list(frame.shape)
del size[2]
size.reverse()
# print(size)
video = cv2.VideoWriter(out_video_full_path, cv2_fourcc, 30, size)

for i in range(len(img)):
    video.write(cv2.imread(img[i]))

video.release()