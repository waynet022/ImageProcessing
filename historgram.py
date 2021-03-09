import cv2 as cv
import matplotlib.pyplot as plt
from spaces import convert_gray

def histogram(image, show=False):
    hist = cv.calcHist([image], [0], None, [256], [0,256])

    if show:
        plt.figure()
        plt.title('Grayscale Histogram')
        plt.xlabel('Bins')
        plt.ylabel('Number of pixels')
        plt.plot(hist)
        plt.xlim([0,256])
        plt.show()

    return hist

if __name__=='__main__':
    image_file = 'assets/images/cats.jpg'
    img = cv.imread(image_file)
    gray = convert_gray(img)
    histogram(img, show=True)