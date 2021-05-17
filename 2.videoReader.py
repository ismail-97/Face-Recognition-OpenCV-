import cv2

cap = cv2.VideoCapture("resource/videos/me.mp4")


while True:
    success, img = cap.read()
    if img is None:
        break
    cv2.imshow("Video Displayer", img)
    if cv2.waitKey(16) & 0xFF == ord ('q'):
        break