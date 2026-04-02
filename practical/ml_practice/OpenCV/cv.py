import cv2 as cv

# # binary Image
# # read image
# img=cv.imread('.venv\practical\ml_practice\OpenCV\ev4.jpg',0) # gray scaled image
# # convert it to binary 
# _,binary=cv.threshold(img,100,255,cv.THRESH_BINARY)
# # show image
# cv.imshow('Image',binary)
# print(type(img))# array
# print(img.shape)
# print(img.dtype)
# print(img.size)
# print(img)
# # save an image
# cv.imwrite('myimg_binary.jpg',binary)

# # grey Scale image
# # read image
# img=cv.imread('.venv\practical\ml_practice\OpenCV\ev4.jpg',0) # gray scaled image
# # show image
# cv.imshow('Image',img)
# print(type(img))# array
# print(img.shape)
# print(img.dtype)
# print(img.size)
# print(img)
# # save an image
# cv.imwrite('myimg_gray.jpg',img)

# Color image
# read image
img=cv.imread('.venv\practical\ml_practice\OpenCV\ev4.jpg') 
# show image
cv.imshow('Image',img)
print(type(img))# array
print(img.shape)
print(img.dtype)
print(img.size)
print(img)
# save an image
# cv.imwrite('myimg_color.jpg',img)

cv.waitKey(0)
cv.destroyAllWindows()
