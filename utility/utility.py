from lobe import ImageModel
from PIL import Image
import cv2


def take_picture():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("/home/pi/sd_rasp/image.jpg", frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def classify_image():
    take_picture()
    model = ImageModel.load('/home/pi/sd_rasp/image_classification')
    img = Image.open('/home/pi/sd_rasp/image.jpg')
    result = model.predict(img)
    labels = [label[0] for label in result.labels]
    confidences = [int(confidence[1]*100) for confidence in result.labels]
    _max = max(confidences)
    if _max > 65:
        label = labels[confidences.index(_max)]
        if label in ["glass"]:
            return "others"
        else:
            return label
    else:
        return "others"
        


