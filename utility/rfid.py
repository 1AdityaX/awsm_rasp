import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class Rfid:
    def __init__(self):
        self.rfid = SimpleMFRC522()

    def read(self):
        try:
            id, text = self.rfid.read()
            data = dict(eval(text))
            return id, data
        finally:
            GPIO.cleanup()
    
    def write(self, data: dict):
    try:
        print("Place your card")
        self.rfid.write(str(data))
        print("Written")
    finally:
        GPIO.cleanup()

    def update_value(self, key, value):
        id, data = self.read()
        updata = data
        updata[key] = value
        self.rfid.write(str(read()))




