import cv2 as cv
import numpy as np
img=cv.imread(r'C:\Users\User\OneDrive\Desktop\programming.jpg')
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
cv.waitKey(0)