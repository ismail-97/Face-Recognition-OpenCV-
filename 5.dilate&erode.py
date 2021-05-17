import cv2
import numpy as np

img = cv2.imread("resource/images/abaya.png")
kernel = np.ones( (5, 5), np.uint8)

#imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#imgBlur = cv2.GaussianBlur(img, (7,7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=2)
imgEroded = cv2.erode(imgDialation, kernel, iterations=2)

#cv2.imshow("gray Image Displayer", imgGray)
#cv2.imshow("blur Image Displayer", imgBlur)
cv2.imshow("Canny Image Displayer", imgCanny)
cv2.imshow("Dialation Image Displayer", imgDialation)
cv2.imshow("Erotion Image Displayer", imgEroded)

cv2.waitKey(0)