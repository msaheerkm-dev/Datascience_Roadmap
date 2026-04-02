# convert image color space to another

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('.venv\practical\ml_practice\OpenCV\ev4.jpg')
img1=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img2=cv.cvtColor(img,cv.COLOR_BGR2HSV)
img3=cv.cvtColor(img,cv.COLOR_BGR2RGB)

cv.imshow('image',img)# normal picture 
cv.imshow('gray',img1)# gray coloured 
cv.imshow('hsv',img2)# hsv coloured 
cv.imshow('rgb',img3)# rgb coloured 

cv.waitKey(0)
cv.destroyAllWindows()