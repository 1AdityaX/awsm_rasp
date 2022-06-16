from utility.utility import classify_image
from utility.servo import Servo
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BCM)
reader = SimpleMFRC522()

lcd = CharLCD('PCF8574', 0x27)

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

    servo1 = Servo(5)
    servo2 = Servo(6)
    top_servo = Servo(13)

    lcd.clear()
    if classfication == "plastic":
        lcd.write_string("Plastic")
        time.sleep(1)
        lcd.clear()
        lcd.write_string("Place it Again to get your points")
        update_points(data, 30)
        servo1.left()
        servo2.left()
        lcd.clear()
        lcd.write_string("You got 30 points")
        time.sleep(1)
        print_lcd_creds(id, data)

    elif classfication == "metal":
        lcd.write_string("Metal")
        time.sleep(1)
        lcd.clear()
        lcd.write_string("Place it Again to get your points")
        update_points(data, 20)
        servo1.left()
        servo2.right()
        lcd.clear()
        lcd.write_string("You got 20 points")
        time.sleep(1)
        print_lcd_creds(id, data)

    elif classfication == "paper" or classfication == "cardboard":
        lcd.write_string("Paper")
        time.sleep(1)
        lcd.clear()
        lcd.write_string("Place it Again to get your points")
        update_points(data, 10)
        servo1.right()
        servo2.left()
        lcd.clear()
        lcd.write_string("You got 10 points")
        time.sleep(1)
        print_lcd_creds(id, data)

    else:
        lcd.write_string("Other")
        time.sleep(1)
        lcd.clear()
        lcd.write_string("Place it Again to get your points")
        update_points(data, 5)
        servo1.right()
        servo2.right()
        lcd.clear()
        lcd.write_string("You got 5 points")
        time.sleep(1)
        print_lcd_creds(id, data)

    top_servo.open()
    top_servo.close()
    servo1.middle()
    servo2.middle()


a = 1

try:
    while a == 1:
        try:
            main()
        except EOFError:
            pass
        except Exception as e:
            raise e            
except KeyboardInterrupt:
    lcd.clear()
    GPIO.cleanup()

