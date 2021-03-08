import cv2 as cv

def average_blur(image, kernel, show=False):
    '''
    higher kernel size will result in blurrier image
    '''
    output = cv.blur(image, (kernel, kernel))
    if show:
        cv.imshow('Average Blur', output)
        cv.waitKey(0)
    return output

def gaussian_blur(image, kernel, sigma=0, show=False):
    '''
    each surrounding pixel has a weight value. The average of the product
    of the weights give the value of the true center. The gaussian method has 
    less blurring than the averaging method, the gaussian blur is more natural.
    '''
    output = cv.GaussianBlur(image, (kernel, kernel), sigma)
    if show:
        cv.imshow('Gaussian Blur', output)
        cv.waitKey(0)
    return output

def median_blur(image, kernel, show=True):
    output = cv.medianBlur(image, kernel)
    if show:
        cv.imshow('Median Blur', output)
        cv.waitKey(0)
    return output

def bilateral_blur(image, diameter, color_sigma, space_sigma, show=False):
    '''
    aims to retain edges of the image
    uses diameter of neighbor pixels
    sigma color, larger value means more color in neighborhood to consider
    '''
    output = cv.bilateralFilter(image, diameter, color_sigma, space_sigma)
    if show:
        cv.imshow('Bilateral Blur', output)
        cv.waitKey(0)
    return output

if __name__=='__main__':
    image_file = 'assets/images/group 1.jpg'
    img = cv.imread(image_file)
    cv.imshow('Original Image', img)
    average_blur(img, 3, show=True)
    gaussian_blur(img, 3, 0, show=True)
    median_blur(img, 3, show=True)
    bilateral_blur(img, 5, 15, 15, show=True)