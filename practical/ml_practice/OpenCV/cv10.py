# i mage histogram

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread('.venv\practical\ml_practice\OpenCV\ev4.jpg',0)

cv.imshow('image',img)

hist=cv.calcHist([img],[0],None,[256],[0,256])

plt.plot(hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()