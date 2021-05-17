import cv2

# here I got an error without cv2.CAP_DSHOW. why?
# also after applying it it becomes more faster at opening the webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640) # width
cap.set(4, 480) # height
cap.set(10, 0)  # resolution

while True:
    success, img = cap.read()

    # to prevent an error
    if img is None: 
        break

    # image mirror
    img = cv2.flip(img,1)

    cv2.imshow("Video Displayer", img)

    if cv2.waitKey(16) & 0xFF == ord ('q'):
        break
