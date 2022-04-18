import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BCM)

class Rfid:
    def __init__(self):
        self.rfid = SimpleMFRC522()
        GPIO.setmode(GPIO.BCM)

    def read(self):
        id, text = self.rfid.read()
        data = dict(eval(text))
        return id, data
    
    def write(self, data: dict):
        print("Place your card")
        self.rfid.write(str(data))
        print("Written")


    def update_value(self, key, value):
        id, data = self.read()
        updata = data
        updata[key] = value
        self.rfid.write(updata)




