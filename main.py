# Custom Imports
from utility.utility import classify_image
from utility.servo import Servo
from utility.sqlite import Sqlite

# PyPi Imports
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import traceback

GPIO.setmode(GPIO.BOARD)
reader = SimpleMFRC522()
lcd = CharLCD('PCF8574', 0x27)
servo1 = Servo(29)
servo2 = Servo(31)
top_servo = Servo(33)
database = Sqlite("awsm.db", "users")

# Points for trash
points = {
    "Plastic": 30,
    "Metal": 20,
    "Paper": 10,
    "Other": 5
}

def print_lcd_creds(data: list):
    lcd.clear()
    lcd.write_string(f'RFID: {data[0]}')
    lcd.cursor_pos = (1, 0)
    lcd.write_string(f'Name: {data[1]}')
    lcd.cursor_pos = (2, 0)
    lcd.write_string(f'Class: {data[2]}')
    lcd.cursor_pos = (3, 0)
    lcd.write_string(f'Points: {data[3]}')
    return

def classify_after_works(trash, data: list):
    lcd.clear()
    lcd.write_string(trash)
    time.sleep(0.5)
    updated_points = data[3] + points[trash]
    database.update_value("points", updated_points, data[0])

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
    time.sleep(0.5)
    up_data = database.get_spec("id", data[0])
    print_lcd_creds(up_data)
    top_servo.open()
    top_servo.close()
    servo1.middle()
    servo2.middle()


def main():
    ids = database.get_attr("id")
    lcd.clear()
    time.sleep(0.5)
    lcd.write_string(u'Place your rfid card')
    time.sleep(0.5)
    id = reader.read_id()
    if id not in ids:
        lcd.clear()
        lcd.write_string(u'Print Card Not found')
        lcd.cursor_pos = (1, 0)
        lcd.write_string(u'Place Your card again to register')
        try:
            id, text = reader.read()
            data_dict = dict(eval(text))
            data_list = [id, data_dict["name"], data_dict["class"], data_dict["points"]]
            database.insert_data(data_list)
            return
        except:
            traceback.print_exc()
            reader.READER.MFRC522_StopCrypto1()
            return

    data = database.get_spec("id", id)
    print_lcd_creds(data)
    classfication = classify_image()
    classify_after_works(classfication, data)

while True:
    try:
        main()
    except KeyboardInterrupt:
        lcd.clear()
        GPIO.cleanup()
        break
    except Exception as e:
        print("Error Caught!")
        traceback.print_exc()
        reader.READER.MFRC522_StopCrypto1()
        print("-----------------------------------------------------------------")
        lcd.clear()
        lcd.write_string('Error Try Again')
    finally:
        GPIO.cleanup()