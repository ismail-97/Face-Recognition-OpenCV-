import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)


#img[200:300, 100:300] = 255, 0, 0
#print(img)

# cv2.line(image, start, end, color, thickness)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]), (0,255,0), 5)

# cv2.rectangle(image, start, end, color, thickness)
cv2.rectangle(img,(100,100),(250, 350), (0,255,0), 5)

#cv2.circle(img, START,radius , color, thickness)
cv2.circle(img, (400,50),30 , (255,255,0), 5)

#cv2.putText(img, TEXT ,START, font , scale ,color, thickness)
cv2.putText(img, " OPENCV", (100,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 150, 0), 3)

cv2.imshow("image", img)

cv2.waitKey(0)