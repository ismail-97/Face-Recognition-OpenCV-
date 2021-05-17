import cv2
import os

# get the face cascade path
cascPathface = os.path.dirname(
 cv2.__file__) + "\data\haarcascade_frontalface_default.xml"
cascPathface2 = os.path.dirname(
 cv2.__file__) + "\data\haarcascade_eye.xml"
# make a cascade classifier using the pre-trained cascade
faceCascade = cv2.CascadeClassifier(cascPathface)
eye_cascade = cv2.CascadeClassifier(cascPathface2)

img = cv2.imread("resource/images/st.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#img = cv2.flip(img, 1)
imgGray = cv2.cvtColor(imgGray, cv2.COLOR_BGR2GRAY)

eyes = eye_cascade.detectMultiScale(img, 1.1, 4)
faces = faceCascade.detectMultiScale(img, 1.02, 8)
#eyes = eyeCascade.detectMultiScale(img)
for (x, y, w, h) in faces:
    for (xx, yy, ww, hh) in eyes:
        if  x <= xx <= x+w and  y <= yy <= y+h: 
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

print(os.path.dirname(cv2.__file__))

cv2.imshow("face detection", img)
cv2.waitKey(0)