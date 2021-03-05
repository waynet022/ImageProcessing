import cv2 as cv
import numpy as np

image_file = 'assets/images/cat.jpg'

# blank image with width, height, and number of color channels
blank = np.zeros((500,500,3), dtype='uint8')

# paint the entire image a certain color
# green
blank[:]=0,255,0
# red
blank[:]=0,0,255

# paint a certain range
blank[200:300, 300:400] = 255,0,0

cv.imshow('Colors', blank)

cv.waitKey(0)