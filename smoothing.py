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

if __name__=='__main__':
    image_file = 'assets/images/group 1.jpg'
    img = cv.imread(image_file)
    cv.imshow('Original Image', img)
    average_blur(img, 3, show=True)