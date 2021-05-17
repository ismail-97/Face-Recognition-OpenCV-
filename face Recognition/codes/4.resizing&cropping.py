import cv2
import numpy as np

img = cv2.imread("resource/images/abaya.png")
print(img.shape)

imgResize = cv2.resize(img, (400,600)) # width first , then height
print(imgResize.shape)

imgCropped = img[0:200, 200:500]     # height first , then width

cv2.imshow("image", imgCropped)
cv2.waitKey(0)