# otsu's Thresholding
# it determine threshold value automaticlly from the grat scale image histogram 
# it seperates image in 2 classes (forground and background based on gray scale itensity value of its pixels)
# it worked well on the image histogram that contains 2 peaks

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread(r'.venv\practical\ml_practice\OpenCV\ev4.jpg',0) 

ret,thresh1=cv.threshold(img,150,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

hist=cv.calcHist([img],[0],None,[256],[0,256])

plt.plot(hist)
plt.show()

cv.imshow('original',img)
cv.imshow('otsus',thresh1)
print(ret)

cv.waitKey(0)
cv.destroyAllWindows()