# video capture using openCV

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

cap=cv.VideoCapture(0)

while True:
    ret,frame=cap.read()

    if not ret:
        print('cannot connect')
        break
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.putText(gray,'SAHEER KM',(100,100),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
    cv.imshow('video',gray)

    if cv.waitKey(1)==ord('p'):
        break

cv.destroyAllWindows()