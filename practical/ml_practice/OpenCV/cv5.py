# resize an image

import numpy as np
import matplotlib.pyplot as plt 
import cv2 as cv

img=cv.imread('.venv\practical\ml_practice\OpenCV\ev4.jpg')

print(img.shape)
# scale=50# DownScale
scale=250 # upscale
# height=int(img.shape[0]*scale/100)
# width=int(img.shape[1]*scale/100)
width=200 # custom width 
height=200 # custom width

dim=(width,height)

res1=cv.resize(img,dim,interpolation=cv.INTER_AREA)

cv.imshow('resized_image',res1)

cv.waitKey(0)
cv.destroyAllWindows()