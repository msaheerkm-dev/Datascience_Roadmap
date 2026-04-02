# image bluring(image smoothing)
# median bluring
# best for salt and pepper image (noise)

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread(r'.venv\practical\ml_practice\OpenCV\ev4.jpg') 


blur=cv.medianBlur(img,25)

cv.imshow('image',img)
cv.imshow('blur',blur)

cv.waitKey(0)
cv.destroyAllWindows()