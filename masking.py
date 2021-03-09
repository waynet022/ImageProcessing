import cv2 as cv
import numpy as np

def mask_image(image, mask, show=False):
    output = cv.bitwise_and(image, image, mask=mask)
    if show:
        cv.imshow('Masked Image', output)
        cv.waitKey(0)
    return output

if __name__=='__main__':
    image_file = 'assets/images/cats.jpg'
    img = cv.imread(image_file)
    blank = np.zeros(img.shape[:2], dtype='uint8')
    mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -2)
    mask_image(img, mask, show=True)