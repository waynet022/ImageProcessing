import cv2 as cv
from spaces import color_space_convert

def threshold_img(gray_image, th_op, thresholds=[90, 255], show=False):
    
    th1=thresholds[0]
    th2=thresholds[1]

    def threshold():
        threshold, thresh = cv.threshold(gray_image, th1, th2, cv.THRESH_BINARY)
        return threshold, thresh
        
    def invert_threshold():
        threshold, inv_thresh = cv.threshold(gray_image, th1, th2, cv.THRESH_BINARY_INV)
        return threshold, inv_thresh
        
    def adaptive_threshold(): return cv.adaptiveThreshold(gray_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
        
    options={
        'binary': threshold,
        'inverted': invert_threshold,
    }

    if th_op == 'adaptive': output = adaptive_threshold()
    else: _, output = options[th_op]()
    
    if show: cv.imshow(' threshold output', output) or cv.waitKey(0)
    
    return output

if __name__=='__main__':
    image_file = 'assets/images/cats.jpg'
    img = cv.imread(image_file)
    gray = color_space_convert(img, 'gray', show=True)
    
    threshold_img(gray, 'adaptive',[], show=True)
    threshold_img(gray, 'binary', [90, 255], show=True)
    threshold_img(gray, 'inverted', [150, 255], show=True)