# image bluring(image smoothing)
# simple bluring

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread(r'.venv\practical\ml_practice\OpenCV\ev4.jpg') 

ksize=(8,8)

blur=cv.blur(img,ksize)

cv.imshow('image',img)
cv.imshow('blur',blur)

cv.waitKey(0)
cv.destroyAllWindows()