from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
lcd = CharLCD(pin_rs=6, pin_rw=5, pin_e=25, pins_data=[16, 26, 13, 12],
              numbering_mode=GPIO.BCM, cols=20, rows=4, auto_linebreaks=True)
#lcd.clear()
lcd.write_string('Place your rfid card')
lcd.clear()

GPIO.cleanup()