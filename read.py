import cv2 as cv

img = cv.imread('assets/images/cat.jpg')

cv.imshow('Cat', img)
cv.waitKey(0)