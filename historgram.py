import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from spaces import color_space_convert

def gray_histogram(image, img_mask=None, show=False):
    hist = cv.calcHist([image], [0], img_mask, [256], [0,256])

    if show:
        plt.figure()
        plt.title('Grayscale Histogram')
        plt.xlabel('Bins')
        plt.ylabel('Number of pixels')
        plt.plot(hist)
        plt.xlim([0,256])
        plt.show()

    return hist

def color_histogram(image, img_mask=None, show=False):
    plt.figure()
    plt.title('Colored Histogram')
    plt.xlabel('Bins')
    plt.ylabel('Number of pixels')
    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist = cv.calcHist([img], [i], img_mask, [256], [0,256])
        plt.plot(hist, color=col)
        plt.xlim(0,256)
    if show:
        plt.show()
    
def circle_mask(image, radius, color=255, thickness=-1, show=False):
    blank = np.zeros(image.shape[:2], dtype='uint8')
    output = cv.circle(blank, (image.shape[1]//2, image.shape[0]//2), radius, color, thickness)
    if show:
        cv.imshow('Circle Mask', output)
        cv.waitKey(0)
    return output

def bitwise_mask_and(image, img_mask, show=False):
    output = cv.bitwise_and(image, image, mask=img_mask)
    if show:
        cv.imshow('And Mask', output)
        cv.waitKey(0)
    return output

if __name__=='__main__':
    image_file = 'assets/images/cats.jpg'
    img = cv.imread(image_file)
    gray = color_space_convert(img, 'gray')
    circle = circle_mask(img, 100)
    bitwise_mask_and(gray, circle)
    color_histogram(img, circle, show=True)