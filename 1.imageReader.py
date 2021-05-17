import cv2

print ("Package Imported")

img = cv2.imread("resource/abaya.png")

cv2.imshow("ImageDisplayer", img)
cv2.waitKey(0) #infinite delay

#cv2.waitKey(1000)  #milliseconds