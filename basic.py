import cv2 as cv

def gray_image(image, show=False):
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

# use as default th1=125, th2=175
def cascade_image(image, th1, th2, show):
    output_image = cv.Canny(image, th1, th2)
    if show:
        cv.imshow('Canny Edges', output_image)
        cv.waitKey(0)
    
    return output_image

def dilate_image(image, kernel_size, iterations=1, show=False):
    output_image = cv.dilate(image, (kernel_size, kernel_size), iterations=iterations)
    if show:
        cv.imshow('Dilated Image', output_image)
        cv.waitKey(0)
    
    return output_image

def erode_image(image, kernel_size, iterations=1, show=False):
    output_image = cv.erode(image, (kernel_size, kernel_size), iterations=iterations)
    if show:
        cv.imshow('Eroded image', output_image)
        cv.waitKey(0)
    
    return output_image

if __name__=='__main__':
    
    image_file = 'assets/images/park.jpg'
    img = cv.imread(image_file)
    
    blur_img = blur_image(img, 7, False)
    cascade = cascade_image(blur_img, 125, 175, False)
    dl = dilate_image(cascade, 7)
    erode_image(dl, 3, show=True)


    
    