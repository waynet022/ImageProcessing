import cv2 as cv
import numpy as np

def bitwise_operation(image_1, image_2, operation, show=False):

    options={
        'and': cv.bitwise_and,
        'or': cv.bitwise_or,
        'xor': cv.bitwise_xor,
    }

    output = options[operation](image_1, image_2)
    if show:
        cv.imshow('Bitwise Operation '+operation, output)
        cv.waitKey(0)
    return output

def bitwise_not(image, show=False):
    output = cv.bitwise_not(image)
    if show:
        cv.imshow('Bitwise not Image', output)
        cv.waitKey(0)
    return output

if __name__=='__main__':
    rect_blank = np.zeros((500,500,3), dtype='uint8')
    circle_blank = np.zeros((500,500,3), dtype='uint8')

    rectangle = cv.rectangle(rect_blank, (10,10), (250,500), (255,255,255), thickness=-1)
    circle = cv.circle(circle_blank, (circle_blank.shape[1]//2, circle_blank.shape[0]//2), 40, (255,255,255), thickness=-1)

    bitwise_operation(rectangle, circle, 'xor', show=True)