from cv2 import VideoCapture
import cv2

def take_picture():
    videoCaptureObject = VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("image.jpg",frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_picture()