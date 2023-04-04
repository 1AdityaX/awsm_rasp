from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time
lcd = CharLCD('PCF8574', 0x27)
lcd.write_string('Place your rfid card')
time.sleep(3)
lcd.clear()

GPIO.cleanup()