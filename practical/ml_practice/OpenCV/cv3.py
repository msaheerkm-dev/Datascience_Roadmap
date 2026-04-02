# split and merge image
import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('.venv\practical\ml_practice\OpenCV\ev4.jpg')
b,g,r=cv.split(img)

img2=cv.merge((b,g,r))

cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

cv.imshow('merge',img2)

cv.waitKey(0)
cv.destroyAllWindows()