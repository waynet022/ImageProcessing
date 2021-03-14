import cv2 as cv
import numpy as np

def display_color_channel(image, color, show=False):
    b,g,r = separate_bgr(image)
    options={
        'blue': b,
        'green': g,
        'red': r
    }

    output = options[color]
    if show:
        cv.imshow(output)
        cv.waitKey(0)
    return output

def separate_bgr(image, show=False):
    '''
    the b,g,r are depicted and displayed as grayscale images that
    show distributions of pixel intensities. 
    Lighter regions means more concentration of those pixel values
    Darker regions means little or no pixel of those values in the region
    '''
    b,g,r = cv.split(image)
    if show:
        cv.imshow('Blue', b)
        cv.imshow('Green', g)
        cv.imshow('Red', r)
        cv.waitKey(0)
    return b,g,r

def merge_channels(ch1, ch2, ch3, show=False):
    merged = [ch1,ch2,ch3]
    output = cv.merge(merged)
    if show:
        cv.imshow('Merged Image', output)
        cv.waitKey(0)
    return output

def bgr_single_channel(image, show=False):
    blank = np.zeros(image.shape[:2], dtype='uint8')
    b,g,r = separate_bgr(image)
    output_b = merge_channels(b, blank, blank)
    output_g = merge_channels(blank, g, blank)
    output_r = merge_channels(blank, blank, r)
    if show:
        cv.imshow('Blue', output_b)
        cv.imshow('Green', output_g)
        cv.imshow('Red', output_r)
        cv.waitKey(0)
    return output_b, output_g, output_r

if __name__=='__main__':
    image_file = 'assets/images/nature4.jfif'
    img=cv.imread(image_file)
    b,g,r = bgr_single_channel(img, show=True)
    b, _, _ = separate_bgr(b)
    _, g, _ = separate_bgr(g)
    _, _, r = separate_bgr(r)
    merge_channels(b,g,r, show=True)
