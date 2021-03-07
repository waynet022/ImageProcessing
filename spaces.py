import cv2 as cv
import matplotlib.pyplot as plt

def convert_gray(image, show=False):
    output = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    if show:
        cv.imshow('Gray Image', output)
        cv.waitKey(0)
    
    return output

def convert_hsv(image, show=False):
    output = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    if show:
        cv.imshow('HSV Image', output)
        cv.waitKey(0)

    return output

def convert_lab(image, show=False):
    output = cv.cvtColor(image, cv.COLOR_BGR2LAB)
    if show:
        cv.imshow('LAB Image', output)
        cv.waitKey(0)
    return output

def show_with_mat(image):
    plt.imshow(image)
    plt.show()

def convert_rgb(image, show=False):
    output = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    if show:
        cv.imshow('RGB Image', output)
        cv.waitKey(0)
    return output

def hsv_convert_bgr(image, show=False):
    output = cv.cvtColor(image, cv.COLOR_HSV2BGR)
    if show:
        cv.imshow('HSV to BGR', output)
        cv.waitKey(0)
    return output

if __name__=='__main__':
    image_file = 'assets/images/park.jpg'
    img = cv.imread(image_file)
    hsv = convert_hsv(img, show=True)
    hsv_convert_bgr(hsv, show=True)
    
    