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

if __name__=='__main__':
    image_file = 'assets/images/lady.jpg'
    img = cv.imread(image_file)
    gray_img = convert_gray(img)
    canny_edge(gray_img, 125, 175, True)