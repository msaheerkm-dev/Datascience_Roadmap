# image bluring(image smoothing)
# Gaussian bluring

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread(r'.venv\practical\ml_practice\OpenCV\ev4.jpg') 

ksize=(9,9)# must be postive & odd number

blur=cv.GaussianBlur(img,ksize,0)

cv.imshow('image',img)
cv.imshow('blur',blur)

cv.waitKey(0)
cv.destroyAllWindows()