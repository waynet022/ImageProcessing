import cv2 as cv

video_file = 'assets/Videos/dog.mp4'
# webcam = integers 0,1,2,etc
# cv.videoCapture(0)

capture = cv.VideoCapture(video_file)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    # key to stop video
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()