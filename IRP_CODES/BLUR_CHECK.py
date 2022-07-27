from brisque import BRISQUE
import cv2 

obj1_iphone = BRISQUE("/Users/kyungyunlee/Desktop/Python_DB/IRP_CODES/IMG_0638.jpg")
obj2_good = BRISQUE("/Users/kyungyunlee/Desktop/Python_DB/IRP_CODES/0piece_middle0.jpg")
obj3_bad = BRISQUE("/Users/kyungyunlee/Desktop/Python_DB/IRP_CODES/0piece_middle1362.jpg")
print("iphone : {}, good : {}, blurred : {}".format(obj1_iphone.score(), obj2_good.score(), obj3_bad.score()))

image_iphone = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/IRP_CODES/IMG_0638.jpg")
image_iphone_gray = cv2.cvtColor(image_iphone, cv2.COLOR_BGR2GRAY)
print(f"iphone: {cv2.Laplacian(image_iphone_gray, cv2.CV_64F).var()}")

image_good = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/IRP_CODES/0piece_middle0.jpg")
image_good_gray = cv2.cvtColor(image_good, cv2.COLOR_BGR2GRAY)
print(f"good: {cv2.Laplacian(image_good_gray, cv2.CV_64F).var()}")

image_blur = cv2.imread("/Users/kyungyunlee/Desktop/Python_DB/IRP_CODES/0piece_middle1362.jpg")
image_blur_gray = cv2.cvtColor(image_blur, cv2.COLOR_BGR2GRAY)
print(f"blur: {cv2.Laplacian(image_blur_gray, cv2.CV_64F).var()}")