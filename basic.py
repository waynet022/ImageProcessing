import cv2 as cv

def convert_to_gray(image, show=False):
    output_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    if show:
        cv.imshow('Gray Image', output_image)
        cv.waitKey(0)
    else:
        return output_image

def blur_image(image, mask, show=False):
    try:
        if mask%2==0:
            raise ValueError
        output_image = cv.GaussianBlur(image, (mask,mask), cv.BORDER_DEFAULT) 
        
        if show:
            cv.imshow('Blurred Image', output_image)
            cv.waitKey(0)
        return output_image
    except ValueError:
        exit('Mask size must be uneven!')

def cascade(image, th1, th2, show):
    output_image = cv.Canny(img, th1, th2)
    if show:
        cv.imshow('Canny Edges', output_image)
        cv.waitKey(0)
    else:
        return output_image


if __name__=='__main__':
    image_file = 'assets/images/cat.jpg'
    img = cv.imread(image_file)
    convert_to_gray(img, True)

    
    