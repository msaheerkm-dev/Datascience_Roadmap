# rotate any image

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread('.venv\practical\ml_practice\OpenCV\ev4.jpg')
# img1=cv.rotate(img,cv.ROTATE_90_CLOCKWISE)
# img2=cv.rotate(img,cv.ROTATE_180)
# img3=cv.rotate(img,cv.ROTATE_90_COUNTERCLOCKWISE)


# cv.imshow('image',img)
# cv.imshow('rotate',img1)
# cv.imshow('rotate_180',img2)
# cv.imshow('rotate_90',img3)

# rotation matrix
print(img.shape)
rows,cols,channels=img.shape
print(rows,cols)
center=(rows/2,cols/2)
print(center)

rm=cv.getRotationMatrix2D(center=center,angle=45,scale=1)

img4=cv.warpAffine(img,rm,(rows,cols))

cv.imshow('rotated_matrix',img4)

cv.waitKey(0)
cv.destroyAllWindows()