import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

cv.rectangle(blank, (10,10), (250,500), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

# to fill the rectangle, thickness = cv.FILLED or -1
cv.rectangle(blank, (10,10), (250,500), (0,255,0), thickness=cv.FILLED)
cv.imshow('Filled Rectangle', blank)
# instead of using coordinates, can also use shape of image
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,0), thickness=cv.FILLED)
cv.imshow('Filled Rectangle using image size', blank)
cv.waitKey(0)