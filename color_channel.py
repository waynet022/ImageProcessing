import cv2 as cv

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

if __name__=='__main__':
    image_file = 'assets/images/park.jpg'
    img=cv.imread(image_file)
    separate_bgr(img, show=True)