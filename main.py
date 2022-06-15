from utility.utility import classify_image
from utility.servo import Servo
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

lcd = CharLCD('PCF8574', 0x27)

def main():
    time.sleep(1)
    lcd.clear()
    time.sleep(1)
    lcd.write_string(u'Place your rfid card')
    time.sleep(2)
    try:
        print("reading")
        id,text = reader.read()
        data = dict(eval(text))
        print(data)
    finally:
        print("fail")
        pass
    lcd.clear()
    
    lcd.write_string(f'RFID: {id}')
    lcd.cursor_pos = (1, 0)
    lcd.write_string(f'Name: {data["name"]}')
    lcd.cursor_pos = (2, 0)
    lcd.write_string(f'Points: {data["points"]}')
    lcd.cursor_pos = (3, 0)
    lcd.write_string(f'Class: {data["class"]}')
    
    classfication = classify_image()

    servo1 = Servo(5)
    servo2 = Servo(6)
    top_servo = Servo(13)

    lcd.clear()
    if classfication == "plastic":
        lcd.write_string("Plastic")
        servo1.left()
        servo2.left()

    elif classfication == "metal":
        lcd.write_string("Metal")
        servo1.left()
        servo2.right()

    elif classfication == "paper" or classfication == "cardboard":
        lcd.write_string("Paper")
        servo1.right()
        servo2.left()

    else:
        lcd.write_string("Other")
        servo1.right()
        servo2.right()

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

