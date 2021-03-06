import cv2 as cv

def convert_gray(image, show=False):
    output = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    if show:
        cv.imshow('Gray Image', output)
        cv.waitKey(0)

    return output

def canny_edge(image, th1=125, th2=175, show=False):
    output = cv.Canny(image, th1, th2)
    if show:
        cv.imshow('Canny Edge', output)
        cv.waitKey(0)

    return output

def find_contours(image, mode='list', approx='none', show=False):
    '''
    mode to find contours:
        tree = cv.RETR_TREE for all the hierarchical contours
        external = cv.RETR_EXTERNAL for all the external contours
        list = cv.RETR_LIST for all contours
    '''
    mode_options = {
        'tree': cv.RETR_TREE,
        'external': cv.RETR_EXTERNAL,
        'list': cv.RETR_LIST
    }
    if mode in mode_options:
        contour_mode = mode_options[mode]
    else:
        contour_mode = cv.RETR_LIST
    '''
    chain approximation methods:
        how to approximate the contours

        cv.CHAIN_APPROX_NONE does nothing and returns all the contours
        cv.CHAIN_APPROX_SIMPLE compresses all the contours that all returned into simple ones that make most sense
        takes all the points of the line and compresses into 1 line from the end points and excludes the points inbetween

    '''
    approximation_methods = {
        'none': cv.CHAIN_APPROX_NONE,
        'simple': cv.CHAIN_APPROX_SIMPLE
    }

    if approx in approximation_methods:
        chain_approx = approximation_methods[approx]
    else:
        chain_approx = cv.CHAIN_APPROX_NONE

    '''
    returns 2 values
        contours is a python list of all the coordinates of all the contours found on the image
        hierarchies refers to the hierarchical representation of contours
    '''
    
    contours, hierarchies = cv.findContours(image, contour_mode, chain_approx)

    return contours, hierarchies

if __name__=='__main__':
    image_file = 'assets/images/lady.jpg'
    img = cv.imread(image_file)
    gray_img = convert_gray(img)
    canny = canny_edge(gray_img, 125, 175)
