import cv2 as cv

cat_image = 'assets/images/cat.jpg'
large_cat_image = 'assets/images/cat_large.jpg'

cat_img = cv.imread(cat_image)
large_cat_img = cv.imread(large_cat_image)

cv.imshow('Cat', cat_img)
cv.imshow('Large Cat', large_cat_img)
cv.waitKey(0)