import cv2 as cv
import numpy as np

def convert_gray(image, show=False):
    output = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    if show:
        cv.imshow('Gray Image', output)
        cv.waitKey(0)
    return output

def laplacian_edge(gray_image, show=False):
    lap = cv.Laplacian(gray_image, cv.CV_64F)
    output = np.uint8(np.absolute(lap))
    if show:
        cv.imshow('Laplacian Edge', output)
        cv.waitKey(0)
    return output

if __name__=='__main__':
    image_file = 'assets/images/cats.jpg'
    img = cv.imread(image_file)
    gray = convert_gray(img, show=True)
    laplacian_edge(gray, show=True)