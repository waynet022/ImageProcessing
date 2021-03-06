import cv2 as cv
import numpy as np


def translate(image, x, y, show=False):
    '''
    -x translate left
    -y translate up
    +x translate right
    +y translate down
    '''
    transMatrix = np.float32([ [1,0,x], [0,1,y] ])
    dimensions = (image.shape[1], image.shape[0])

    output = cv.warpAffine(image, transMatrix, dimensions)

    if show:
        cv.imshow('Translated image', output)
        cv.waitKey(0)

    return output

def rotate(image, angle, rotPoint=None, show=False):
    (height, width) = image.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    output = cv.warpAffine(image, rotMatrix, dimensions)
    if show:
        cv.imshow('Rotate Image', output)
        cv.waitKey(0)
    
    return output

def flip_image(image, flip_value, show=False):
    '''
    for flip value code:
        0 flip vertically, over x axis
        1 flip horizontally, over y axis
        -1 flip both vertically and horizontally
    '''
    output = cv.flip(image, flip_value)
    if show:
        cv.imshow('Flipped image', output)
        cv.waitKey(0)

    return output

if __name__=='__main__':
    image_file = 'assets/images/park.jpg'
    img = cv.imread(image_file)
    
    translated = translate(img, 100, 100, True)
    rotated = rotate(img, 45)
    rotated = rotate(rotated, 45, show=True)
    flip = flip_image(img, 1, show=True)