import cv2 as cv

image_file = 'assets/images/cat.jpg'
img = cv.imread(image_file)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Original image', img)
cv.imshow('Gray image', gray)
cv.waitKey(0)