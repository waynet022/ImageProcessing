import cv2 as cv
import matplotlib.pyplot as plt

def color_space_convert(image, conversion, show=False):
    
    options={
        'gray': cv.COLOR_BGR2GRAY,
        'hsv': cv.COLOR_BGR2HSV,
        'lab': cv.COLOR_BGR2LAB,
        'rgb': cv.COLOR_BGR2RGB
    }
    if conversion=='original':
        output=image
    else:
        color_space=options[conversion]
        output = cv.cvtColor(image, color_space)
    if show:
        cv.imshow('Converted Image', output)
        cv.waitKey(0)
    return output

def show_with_mat(image):
    plt.imshow(image)
    plt.show()

def hsv_convert_bgr(image, show=False):
    output = cv.cvtColor(image, cv.COLOR_HSV2BGR)
    if show:
        cv.imshow('HSV to BGR', output)
        cv.waitKey(0)
    return output

def lab_convert_bgr(image, show=False):
    output = cv.cvtColor(image, cv.COLOR_LAB2BGR)
    if show:
        cv.imshow('LAB to BGR', output)
        cv.waitKey(0)
    return output

if __name__=='__main__':
    image_file = 'assets/images/park.jpg'
    img = cv.imread(image_file)
    lab = color_space_convert(img, 'lab', show=True)
    lab_convert_bgr(lab, show=True)
    