from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
lcd = CharLCD(pin_rs=31, pin_rw=29, pin_e=22, pins_data=[36, 37, 33, 32],
              numbering_mode=GPIO.BOARD, cols=20, rows=4, auto_linebreaks=True)
#lcd.clear()
lcd.write_string('Place your rfid card')
lcd.clear()

GPIO.cleanup()