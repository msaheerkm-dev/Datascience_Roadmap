# Adaptive thresholding

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread(r'.venv\practical\ml_practice\OpenCV\ev4.jpg',0) 

thresh1=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,77,5)

cv.imshow('original',img)
cv.imshow('Adaptive',thresh1)

cv.waitKey(0)
cv.destroyAllWindows()  