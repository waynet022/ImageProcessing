import cv2 as cv
import numpy as np

image = 'assets/photos/marleny3.jpg'
img = cv.imread(image)

cv.imshow('Wife', img)

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('rotation', rotated)

newrotated = rotate(rotated, -45)
cv.imshow('rotation2', newrotated)

cv.waitKey(0)