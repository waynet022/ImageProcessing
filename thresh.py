import cv2 as cv
from spaces import color_space_convert

def threshold_img(gray_image, th1, th2, show=False):
    threshold, thresh = cv.threshold(gray_image, th1, th2, cv.THRESH_BINARY)
    if show:
        cv.imshow('Threshold Image', thresh)
        cv.waitKey(0)
    return threshold, thresh

def invert_threshold_img(gray_image, th1, th2, show=False):
    threshold, inv_thresh = cv.threshold(gray_image, th1, th2, cv.THRESH_BINARY_INV)
    if show:
        cv.imshow('Inverted Threshold Image', inv_thresh)
        cv.waitKey(0)
    return threshold, inv_thresh

def adaptive_threshold_img(gray_image, show=False):
    output = cv.adaptiveThreshold(gray_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
    if show:
        cv.imshow('Adaptive Thresholding', output)
        cv.waitKey(0)
    return output

if __name__=='__main__':
    image_file = 'assets/images/cats.jpg'
    img = cv.imread(image_file)
    gray = color_space_convert(img, 'gray', show=True)
    threshold_img(gray, 90, 255, show=True)
    invert_threshold_img(gray, 150, 255, show=True)
    adaptive_threshold_img(gray, show=True)