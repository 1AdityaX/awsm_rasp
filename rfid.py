import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    name = input('Enter the name: ')
    grade = input('Enter the class: ')
    data = {
        "name": name,
        "points": 0,
        "class": grade,
        
    }
    print("Now place your tag to write")
    reader.write(str(data))
    print("Written")
finally:
    GPIO.cleanup()