import cv2

img = cv2.imread("resource/images/abaya.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (7,7), 0)

cv2.imshow("gray Image Displayer", imgGray)
cv2.imshow("blur Image Displayer", imgBlur)

cv2.waitKey(0)