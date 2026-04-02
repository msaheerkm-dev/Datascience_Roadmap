# color detection using hsv color space
# hue - represents the colour
# saturation - represents the grayness
# value - rpresents the darkness
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread(r'.venv\practical\ml_practice\OpenCV\Color_detection\images.jpg')

def findred(img):
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

    # red colour range
    lower_range=(0,100,100)
    upper_range=(10,255,255)
    # creating a mask
    mask=cv.inRange(hsv,lower_range,upper_range)
    mask1=cv.medianBlur(mask,9)

# find contours
    contours,_=cv.findContours(mask1,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

# draw rectangle
    if contours:
         cnt=contours[0]
         x,y,w,h=cv.boundingRect(cnt)
         cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
         cv.putText(img,'RED',(x,y),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    else:
         print('colour not detected')

def findyellow(img):
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

    # red colour range
    lower_range=(25,100,100)
    upper_range=(35,255,255)
    # creating a mask
    mask=cv.inRange(hsv,lower_range,upper_range)
    mask1=cv.medianBlur(mask,9)

# find contours
    contours,_=cv.findContours(mask1,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

# draw rectangle
    if contours:
         cnt=contours[0]
         x,y,w,h=cv.boundingRect(cnt)
         cv.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
         cv.putText(img,'yellow',(x,y),cv.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)
    else:
         print('colour not detected')

def fingGreen(img):
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

    # red colour range
    lower_range=(45,100,100)
    upper_range=(65,255,255)
    # creating a mask
    mask=cv.inRange(hsv,lower_range,upper_range)
    mask1=cv.medianBlur(mask,9)

# find contours
    contours,_=cv.findContours(mask1,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

# draw rectangle
    if contours:
         cnt=contours[0]
         x,y,w,h=cv.boundingRect(cnt)
         cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
         cv.putText(img,'green',(x,y),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    else:
         print('colour not detected')

findred(img)
findyellow(img)
fingGreen(img)

cv.imshow('image',img)
# cv.imshow('mask',mask)
# cv.imshow('mask1',msk_image)

cv.waitKey(0)
cv.destroyAllWindows()