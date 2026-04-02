# hand landmark using mediapipe

import numpy as np
import matplotlib.pyplot as plt 
import cv2 as cv

cap=cv.VideoCapture(0)

while True:
    ret,frame=cap.read()

    if not ret:
        print('cannot read')
        break

    frame=cv.flip(frame,1)

    cv.imshow('video',frame)

    if cv.waitKey(1)==ord('p'):
        break


cv.destroyAllWindows()




