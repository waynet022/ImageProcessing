import cv2 as cv
import numpy as np


def translate(image, x, y):
    '''
    -x translate left
    -y translate up
    +x translate right
    +y translate down
    '''
    transMatrix = np.float32([ [1,0,x], [0,1,y] ])
    dimensions = (image.shape[1], image.shape[0])

    return cv.warpAffine(image, transMatrix, dimensions)

if __name__=='__main__':
    image_file = 'assets/images/park.jpg'
    img = cv.imread(image_file)
    
    translated = translate(img, 100, 100)
    cv.imshow('Boston', translated)
    cv.waitKey(0)


