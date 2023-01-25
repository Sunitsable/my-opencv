import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')  #syntax of numpy zeroes array is a=np.zeros(n,dtype) n is the no of elements u want zeros

#cv.imshow('blank',blank)   #imshow creates a gui window and displays the image, syntax is cv.imshow('any name of a window ',the name of the pixels stored)

blank[200:300,300:400]=0,255,255  #here array slicing is done first out of 500 rows and 500 columns array if we take the arrays from 200 to 299 index and select the elemnts of index 300:400 and then we color it by array slicing
cv.imshow('green',blank)

cv.waitKey(0)  #here capital k is very important