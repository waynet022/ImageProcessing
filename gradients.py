import cv2 as cv
import numpy as np
from bitwise import bitwise_or
from spaces import color_space_convert

def laplacian_edge(gray_image, show=False):
    lap = cv.Laplacian(gray_image, cv.CV_64F)
    output = np.uint8(np.absolute(lap))
    if show:
        cv.imshow('Laplacian Edge', output)
        cv.waitKey(0)
    return output

def sobel_x(gray_image, show=False):
    output = cv.Sobel(gray_image, cv.CV_64F, 1, 0)
    if show:
        cv.imshow('Sobel X', output)
        cv.waitKey(0)
    return output

def sobel_y(gray_image, show=False):
    output = cv.Sobel(gray_image, cv.CV_64F, 0, 1)
    if show:
        cv.imshow('Sobel X', output)
        cv.waitKey(0)
    return output

def canny_edge(gray_image, show=False):
    output = cv.Canny(gray_image, 150, 175)
    if show:
        cv.imshow('Canny Edge', output)
        cv.waitKey(0)
    return output

if __name__=='__main__':
    image_file = 'assets/images/park.jpg'
    img = cv.imread(image_file)
    gray = color_space_convert(img, 'gray', show=False)
    canny_edge(gray, show=True)