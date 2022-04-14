import RPi.GPIO as GPIO
import time

sensor = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)

print("IR Sensor Ready.....")


try: 
   while True:
      if GPIO.input(sensor):
          print("Object Detected")
          while GPIO.input(sensor):
              time.sleep(0.2)


except KeyboardInterrupt:
    GPIO.cleanup()