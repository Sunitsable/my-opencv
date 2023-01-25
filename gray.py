import cv2 as cv
import numpy as np
img=cv.imread(r'C:\Users\User\OneDrive\Desktop\me.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
cv.waitKey(0)
#canny edges detection
canny=cv.Canny('img',25,75)
cv.imshow('canny',canny)
cv.waitKey(0)
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
cv.waitKey(0)
#resizing the img
resized=cv.resize(img,(1000,500))
cv.imshow('img',resized)
cv.waitKey(0)
