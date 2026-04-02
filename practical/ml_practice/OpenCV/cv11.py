# image Thresholding(binarising image (0-255) only)
# simple thresholding

import numpy as np
import matplotlib.pyplot as plt 
import cv2 as cv

img=cv.imread('.venv\practical\ml_practice\OpenCV\ev4.jpg',0)

ret,thresh1=cv.threshold(img,120,255,cv.THRESH_BINARY)
ret,thresh2=cv.threshold(img,120,255,cv.THRESH_BINARY_INV)
ret,thresh3=cv.threshold(img,120,255,cv.THRESH_TRUNC)
ret,thresh4=cv.threshold(img,120,255,cv.THRESH_TOZERO)
ret,thresh5=cv.threshold(img,120,255,cv.THRESH_TOZERO_INV)

cv.imshow('original',img)
cv.imshow('Binary_threshold',thresh1)
cv.imshow('Binary_INV_threshold',thresh2)
cv.imshow('TRUNC_threshold',thresh3)
cv.imshow('TOZERO_threshold',thresh4)
cv.imshow('TOZERO_INV_threshold',thresh5)

cv.waitKey(0)
cv.destroyAllWindows()

