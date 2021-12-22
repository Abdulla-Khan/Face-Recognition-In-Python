import cv2
import numpy as np
import winsound
f =2500
d = 10
fc = cv2.CascadeClassifier('cv.xml')
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = fc.detectMultiScale(gray,1.1,5)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    if np.array(face).size:
        winsound.Beep(f,d)
        cv2.putText(frame,'Number of Faces : ' + str(len(face)),(40, 40), font, 1,(255,0,0),2)      

    cv2.imshow('img',frame)

    k=cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()