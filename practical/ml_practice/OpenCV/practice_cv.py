import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread(r'.venv\practical\ml_practice\OpenCV\ev4.jpg',0) 

# _,sm_thrsh=cv.threshold(img,200,255,cv.THRESH_BINARY)

# ad_thrsh=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,77,5)

# _,otsus=cv.threshold(img,150,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# cv.imshow('image',sm_thrsh)
# cv.imshow('image1',ad_thrsh)
# cv.imshow('image2',otsus)




cv.waitKey(0)
cv.destroyAllWindows()
