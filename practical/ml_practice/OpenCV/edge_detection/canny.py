# canny edge detection
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread(r'.venv\practical\ml_practice\OpenCV\ev4.jpg',0)

edge=cv.Canny(img,120,200)

cv.imshow('blur',edge)

cv.waitKey(0)
cv.destroyAllWindows()