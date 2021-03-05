import cv2 as cv
import numpy as np

rect_blank = np.zeros((500,500,3), dtype='uint8')

cv.rectangle(rect_blank, (10,10), (250,500), (0,255,0), thickness=2)
cv.imshow('Rectangle', rect_blank)

fill_blank = np.zeros((500,500,3), dtype='uint8')
# to fill the rectangle, thickness = cv.FILLED or -1
cv.rectangle(fill_blank, (10,10), (250,500), (0,255,0), thickness=cv.FILLED)
cv.imshow('Filled Rectangle', fill_blank)

shape_blank = np.zeros((500,500,3), dtype='uint8')
# instead of using coordinates, can also use shape of image
cv.rectangle(shape_blank, (0,0), (shape_blank.shape[1]//2, shape_blank.shape[0]//2), (255,255,0), thickness=cv.FILLED)
cv.imshow('Filled Rectangle using image size', shape_blank)

circle_blank = np.zeros((500,500,3), dtype='uint8')
# circle
cv.circle(circle_blank, (circle_blank.shape[1]//2, circle_blank.shape[0]//2), 40, (0,255,0), thickness=3)
cv.imshow('Circle', circle_blank)

line_blank = np.zeros((500,500,3), dtype='uint8')
# line
cv.line(line_blank, (0,0), (line_blank.shape[1]//2, line_blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', line_blank)

text_blank = np.zeros((500,500,3), dtype='uint8')
# write text on image
cv.putText(text_blank, 'hello', (200,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
cv.imshow('Text on image', text_blank)

cv.waitKey(0)