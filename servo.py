import RPi.GPIO as GPIO
from utility.servo import Servo 

GPIO.setmode(GPIO.BCM)
servo = Servo(17)
servo.open()
servo.close()