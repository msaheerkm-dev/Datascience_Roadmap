# adding text to the image

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread('.venv\practical\ml_practice\OpenCV\ev4.jpg')

cv.putText(img,'LEARN OPENCV',(20,80),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv.imshow('image',img)

cv.waitKey(0)
cv.destroyAllWindows()