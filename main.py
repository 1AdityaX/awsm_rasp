# Custom Imports
from utility.utility import classify_image
from utility.servo import Servo

# PyPi Imports
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

# Pin Setups
GPIO.setmode(GPIO.BOARD)
reader = SimpleMFRC522()
servo1 = Servo(29)
servo2 = Servo(31)
top_servo = Servo(33)
lcd = CharLCD('PCF8574', 0x27)
_rfid_RST_pin = 22

# Points for trash
points = {
    "Plastic": 30,
    "Metal": 20,
    "Paper": 10,
    "Other": 5
}


def print_lcd_creds(id, data: dict):
    lcd.clear()
    lcd.write_string(f'RFID: {id}')
    lcd.cursor_pos = (1, 0)
    lcd.write_string(f'Name: {data["name"]}')
    lcd.cursor_pos = (2, 0)
    lcd.write_string(f'Points: {data["points"]}')
    lcd.cursor_pos = (3, 0)
    lcd.write_string(f'Class: {data["class"]}')
    

def update_points(data: dict, points):
    data["points"] = int(data["points"]) + points
    try:
        reader.write(str(data))
    finally:
        pass


def classify_after_works(trash, data):
    lcd.write_string(trash)
    time.sleep(1)
    lcd.clear()
    lcd.write_string("Place it Again to get your points")
    update_points(data, points[trash])

    if trash == "Plastic":
        servo1.right()
        servo2.left()
    elif trash == "Metal":
        servo1.left()
        servo2.right()
    elif trash == "Paper":
        servo1.right()
        servo2.left()
    else:
        servo1.right()
        servo2.right()

    lcd.clear()
    lcd.write_string(f"You got {points[trash]} points")
    time.sleep(1)
    print_lcd_creds(id, data)
    top_servo.open()
    top_servo.close()
    servo1.middle()
    servo2.middle()


def main():
    time.sleep(1)
    lcd.clear()
    time.sleep(1)
    lcd.write_string(u'Place your rfid card')
    time.sleep(2)
    try:
        id,text = reader.read()
        data = dict(eval(text))
    finally:
        pass
    print_lcd_creds(id, data)
    
    classfication = classify_image()
    lcd.clear()

    classify_after_works(classfication, data)



while True:
    try:
        main()
    except EOFError:
        pass
    except KeyboardInterrupt:
        lcd.clear()
        GPIO.cleanup()
        break
    except Exception as e:
        print(e)
        GPIO.setup(_rfid_RST_pin, GPIO.OUT)
        GPIO.output(_rfid_RST_pin, GPIO.LOW)
        lcd.clear()
        lcd.write_string('Error Try Again')



