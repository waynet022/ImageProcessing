import cv2 as cv


#for videos, images, and live videos
def rescale_frame(frame, scale=1):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def rescale_video(video_file, scale):
    capture = cv.VideoCapture(video_file)

    while True:
        isTrue, frame = capture.read()

        frame_resized = rescale_frame(frame, scale)
        cv.imshow('Rescaled Video', frame_resized)

        if cv.waitKey(20) & 0xFF==ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()

if __name__=='__main__':
    video_file = 'assets/videos/dog.mp4'
    scale = 0.55
    rescale_video(video_file, scale)