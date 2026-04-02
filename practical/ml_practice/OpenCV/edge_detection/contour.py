# contour detection process
# original - gray - canny/threshold - contour

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread(r'.venv\practical\ml_practice\OpenCV\ev4.jpg') # original

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) # gray scale image

ret,thresh=cv.threshold(gray,200,255,cv.THRESH_BINARY_INV) # threshold image

contours,_=cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img,contours,-1,(0,255,0),3)

print(len(contours))

cv.imshow('img',img)
cv.imshow('gray',gray)
cv.imshow('threshold',thresh)


cv.waitKey(0)
cv.destroyAllWindows()