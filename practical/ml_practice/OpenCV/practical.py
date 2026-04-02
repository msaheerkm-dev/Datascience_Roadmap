import cv2 as cv
import numpy as np

img=cv.imread(r'.venv\practical\ml_practice\OpenCV\ev4.jpg')

print(img.shape)


rez_img=cv.resize(img,(200,200),cv.INTER_AREA) # resized image (200,200)

crop=img[0:100,0:100] # clipped image

rez_org_img=cv.resize(img,(300,168),cv.INTER_LINEAR) # resized to original image

cv.imshow('original_image',img)
cv.imshow('resized_image',rez_img)
cv.imshow('image_cropped',crop)
cv.imshow('resized_org_img',rez_org_img)

# cv.imshow('image3',rez_org_img)

cv.waitKey(0)
cv.destroyAllWindows()