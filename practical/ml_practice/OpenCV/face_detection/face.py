# face detection using haar cascade classifier

import numpy as n
import matplotlib.pyplot as plt 
import cv2 as cv

cap=cv.VideoCapture(0)

face_cascade=cv.CascadeClassifier(r'.venv\practical\ml_practice\OpenCV\face_detection\haarcascade_frontalface_default.xml')

while True:
    ret,frame=cap.read()

    if not ret:
        print('cannot connect')

    # gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(frame,1.3,4)

    for x,y,w,h in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv.imshow('Video',frame)
    if cv.waitKey(1)==ord('p'):
        break

cap.release()
cv.destroyAllWindows()



