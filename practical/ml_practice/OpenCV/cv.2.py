# accesing pixel values
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('.venv\practical\ml_practice\OpenCV\ev4.jpg')
img1=img[50:125,125:300] # image slicing

plt.imshow(img1)
plt.show()

# cv.imshow('Image',img) # in opencv it is in BGR format
# cv.waitKey(0)
# cv.destroyAllWindows()