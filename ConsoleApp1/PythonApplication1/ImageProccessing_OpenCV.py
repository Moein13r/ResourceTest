import cv2
import numpy as np
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened():  # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
PrevX = 0
while rval:
    frame = np.fliplr(frame)
    Mainimg = frame
    width = frame.shape[0]
    faces = faceCascade.detectMultiScale(
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30),
    )
    for x, y, w, h in faces:
        print("in for", end=" ")
        print(x, end=" ")
        print(y, end="\n")
        if x > PrevX:
            print('right')
        else:
            print('left')

        Mainimg = np.array(Mainimg)
        cv2.circle(Mainimg,(x+80,y+60),100,(0,0,255), thickness=1)
        cv2.rectangle(Mainimg, (x, y), (x+w, y+h), (0, 255, 255), 2)
        PrevX = x
    cv2.imshow("preview", Mainimg)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
        break

vc.release()
cv2.destroyWindow("preview")
