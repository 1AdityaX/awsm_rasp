from lobe import ImageModel
from PIL import Image

model = ImageModel.load('/home/pi/sd_rasp/image_classification')


# OPTION 3: Predict from Pillow image

img = Image.open('/home/pi/sd_rasp/image.jpg')

result = model.predict(img)

# Print top prediction
print(result.prediction)

# Print all classes
for label, confidence in result.labels:
    print(f"{label}: {confidence*100}%")


