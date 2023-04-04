from utility.utility import classify_image
from utility.servo import Servo
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


lcd = CharLCD('PCF8574', 0x27)

def main():
    time.sleep(1)
    lcd.clear()
    time.sleep(1)
    lcd.write_string(u'Running backup...')
    lcd.clear()
    time.sleep(2)
    lcd.write_string(u'Place your trash in the deposit box')
    time.sleep(4)
    classfication = classify_image()

    servo1 = Servo(5)
    servo2 = Servo(6)
    top_servo = Servo(13)

    lcd.clear()
    if classfication == "plastic":
        lcd.write_string("Plastic")
        servo1.left()
        servo2.left()
        time.sleep(1)
        lcd.clear()

    elif classfication == "metal":
        lcd.write_string("Metal")
        servo1.left()
        servo2.right()
        time.sleep(1)
        lcd.clear()

    elif classfication == "paper" or classfication == "cardboard":
        lcd.write_string("Paper")
        servo1.right()
        servo2.left()
        time.sleep(1)
        lcd.clear()

    else:
        lcd.write_string("Other")
        servo1.right()
        servo2.right()
        time.sleep(1)
        lcd.clear()

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

