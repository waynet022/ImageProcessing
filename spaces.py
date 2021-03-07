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

def show_with_mat(image):
    plt.imshow(image)
    plt.show()

if __name__=='__main__':
    image_file = 'assets/images/park.jpg'
    img = cv.imread(image_file)
    convert_gray(img, show=True)
    convert_hsv(img, show=True)
    convert_lab(img, show=True)
    show_with_mat(img)