import cv2 as cv
import numpy as np

image = 'assets/photos/marleny3.jpg'
img = cv.imread(image)

cv.imshow('wife', img)

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)

cv.imshow('translated',resized)

# 0 = vertical flip
# 1 = horizontal flip
# -1 = both vertical and horizontal flip
flip = cv.flip(img, -1)
cv.imshow('translated', flip)

cropped = img[10:500, 100:500]
cv.imshow('cropped', cropped)


cv.waitKey(0)