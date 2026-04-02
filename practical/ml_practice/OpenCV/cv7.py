# draw figures using cv
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread('.venv\practical\ml_practice\OpenCV\ev4.jpg')

# # to draw line
# cv.line(img,(20,150),(125,200),(255,0,0),5)

# # to draw a reactangle
# cv.rectangle(img,(20,20),(200,150),(255,0,0),-1)

# to draw a circle 
# cv.circle(img,(100,80),70,(255,0,0),-1)

# to draw an ellipse
# cv.ellipse(img,(100,80),(70,30),0,0,366,(255,0,0),-1)

# construct figures using cv.line
# cv.line(img,(50,140),(150,20),(255,0,0),2)
# cv.line(img,(150,20),(250,140),(255,0,0),2)
# cv.line(img,(250,140),(50,140),(255,0,0),2)

pts=np.array([[50,140],[150,20],[250,140]])
cv.polylines(img,[pts],True,(0,0,255),2)

plt.imshow(img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()