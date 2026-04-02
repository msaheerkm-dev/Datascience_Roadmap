# creating image with array
import cv2 as cv
import numpy as np

# # black image
# img=np.zeros((500,500),dtype='uint8')
# cv.imshow('black',img)

# # white image
# img=255*np.ones((500,500),dtype='uint8')
# cv.imshow('White',img)

# grey image
img=150*np.ones((500,500),dtype='uint8')
cv.imshow('Grey',img)

cv.waitKey(0)
cv.destroyAllWindows()


