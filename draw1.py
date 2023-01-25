import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
#drawing a rectangle
cv.rectangle(blank, (0,0), (250,250),(0,255,255),thickness=2) 
cv.imshow('rectangle',blank)
cv.waitKey(0)
#drawing a circle
cv.circle(blank,(250,250),250,(0,0,255),thickness=2) #for thickness to be full use thickness=cv.FILLED

cv.imshow('circle',blank)
cv.waitKey(0)
#COMMON SYNTAX OF THESE METHODS
#cv.shape('array of pixels',startpt,endpt,color,thickness)
