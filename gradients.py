import cv2 as cv
import numpy as np
from bitwise import bitwise_operation
from spaces import color_space_convert

def compute_gradient(img, gradient, show=False):
        
    def laplacian_edge(gray_image, show=False):
        lap = cv.Laplacian(gray_image, cv.CV_64F)
        output = np.uint8(np.absolute(lap))
        return output

    def sobel_x(gray_image): return cv.Sobel(gray_image, cv.CV_64F, 1, 0)

    def sobel_y(gray_image): return cv.Sobel(gray_image, cv.CV_64F, 0, 1)        

    def canny_edge(gray_image): return cv.Canny(gray_image, 150, 175)
    
    def sobel_xy(gray_image):
        sobelx = sobel_x(gray_image)
        sobely = sobel_y(gray_image)
        output = bitwise_operation(sobelx, sobely, 'or')
        return output

    options={
        'laplacian': laplacian_edge(img),
        'sobelx': sobel_x(img),
        'sobely': sobel_y(img),
        'sobelxy': sobel_xy(img),
        'canny': canny_edge(img)
    }
    
    output=options[gradient]
    if show:
        cv.imshow('Gradient Image', output)
        cv.waitKey(0)
    return output

if __name__=='__main__':
    image_file = 'assets/images/nature6.jfif'
    img = cv.imread(image_file)
    gray = color_space_convert(img, 'gray')
    compute_gradient(gray, 'canny',show=True)