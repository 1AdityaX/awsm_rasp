import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import json

reader = SimpleMFRC522()

try:
    id, text = reader.read()
    print(id)
    try:
        data = dict(eval(text))
        for k, v in data.items():
            print(f"{k} \t {v}")
    except ValueError:
        print(text)
finally:
    GPIO.cleanup()