import cv2 as cv

def convert_gray(image, show=False):
    output = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    if show:
        cv.imshow('Gray Image', output)
        cv.waitKey(0)
    return output

def threshold_img(gray_image, th1, th2, show=False):
    threshold, thresh = cv.threshold(gray_image, th1, th2, cv.THRESH_BINARY)
    if show:
        cv.imshow('Threshold Image', thresh)
        cv.waitKey(0)
    return threshold, thresh

if __name__=='__main__':
    image_file = 'assets/images/cats.jpg'
    img = cv.imread(image_file)
    gray = convert_gray(img, show=True)
    threshold_img(gray, 90, 255, show=True)