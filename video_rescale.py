import cv2 as cv


capture = cv.VideoCapture(0)

def changeRes(width, height):
    # only for live videos
    capture.set(3,width)
    capture.set(4,height)