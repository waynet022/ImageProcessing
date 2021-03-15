import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from spaces import color_space_convert
from bitwise import bitwise_operation

def show_histogram(image, channel, img_mask=None):

    def gray_histogram():
        gray_image = (image if len(image.shape) < 3 else color_space_convert(image, 'gray'))
        hist = cv.calcHist([gray_image], [0], img_mask, [256], [0,256])

        plt.figure()
        plt.title('Grayscale Histogram')
        plt.xlabel('Bins')
        plt.ylabel('Number of pixels')
        plt.plot(hist)
        plt.xlim([0,256])
        plt.show()

    def color_histogram():
        plt.figure()
        plt.title('Colored Histogram')
        plt.xlabel('Bins')
        plt.ylabel('Number of pixels')
        colors = ('b', 'g', 'r')
        for i, col in enumerate(colors):
            hist = cv.calcHist([image], [i], img_mask, [256], [0,256])
            plt.plot(hist, color=col)
            plt.xlim(0,256)
        plt.show()
        
    def circle_mask(radius, color=255, thickness=-1, show=False):
        blank = np.zeros(image.shape[:2], dtype='uint8')
        output = cv.circle(blank, (image.shape[1]//2, image.shape[0]//2), radius, color, thickness)
        if show:
            cv.imshow('Circle Mask', output)
            cv.waitKey(0)
        return output
    # circle = circle_mask(img, 100, show=True)
    # bitwise_and(gray, circle)

    if channel=='color':
        color_histogram()
    if channel=='gray':
        gray_histogram()

if __name__=='__main__':
    image_file = 'assets/images/cats.jpg'
    img = cv.imread(image_file)
    gray = color_space_convert(img, 'gray')
    show_histogram(img, 'color')