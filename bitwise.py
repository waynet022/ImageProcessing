import cv2 as cv
import numpy as np

def create_rectangle(image,start, end, color=255, thickness=-1, show=False):
    output = cv.rectangle(image.copy(), start, end, color, thickness)
    if show:
        cv.imshow('Rectangle', output)
        cv.waitKey(0)
    return output

def create_circle(image, center, radius, color=255, thickness=-1, show=False):
    output = cv.circle(image.copy(), center, radius, 255, -1)
    if show:
        cv.imshow('Circle', output)
        cv.waitKey(0)
    return output

def bitwise_and(image_1, image_2, show=False):
    output = cv.bitwise_and(image_1, image_2)
    if show:
        cv.imshow('Bitwise And Image', output)
        cv.waitKey(0)
    return output

def bitwise_or(image_1, image_2, show=False):
    output = cv.bitwise_or(image_1, image_2)
    if show:
        cv.imshow('Bitwise Or Image', output)
        cv.waitKey(0)
    return output

def bitwise_xor(image_1, image_2, show=False):
    output = cv.bitwise_xor(image_1, image_2)
    if show:
        cv.imshow('Bitwise xor Image', output)
        cv.waitKey(0)
    return output

def bitwise_not(image, show=False):
    output = cv.bitwise_not(image)
    if show:
        cv.imshow('Bitwise not Image', output)
        cv.waitKey(0)
    return output

if __name__=='__main__':
    blank = np.zeros((400,400), dtype='uint8')
    rectangle = create_rectangle(blank, (30,30), (370,370))
    circle = create_circle(blank, (200,200), 200)
    bitwise_and(rectangle, circle, show=True)
    bitwise_or(rectangle, circle, show=True)
    bitwise_xor(rectangle, circle, show=True)
    bitwise_not(circle, show=True)