import RPi.GPIO as GPIO
import time

class Servo():
    def __init__(self, servopin):
        self.servopin = servopin
        GPIO.setmode(GPIO.BCM)
        

    def right(self):
        pin = self.servopin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servopin, GPIO.OUT)
        pwm = GPIO.PWM(self.servopin, 50)
        pwm.start(0)
        try: 
            pwm.ChangeDutyCycle(5.5)
            time.sleep(1)
            pwm.stop()
        except KeyboardInterrupt:
            pwm.stop()
            GPIO.cleanup()
        
    def left(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servopin, GPIO.OUT)
        pwm = GPIO.PWM(self.servopin, 50)
        pwm.start(0)
        try: 
            pwm.ChangeDutyCycle(10.5)
            time.sleep(1)
            pwm.stop()
        except KeyboardInterrupt:
            pwm.stop()
            GPIO.cleanup()

    def middle(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servopin, GPIO.OUT)
        pwm = GPIO.PWM(self.servopin, 50)
        pwm.start(0)
        try: 
            pwm.ChangeDutyCycle(7.6)
            time.sleep(1)
            pwm.stop()
        except KeyboardInterrupt:
            pwm.stop()
            GPIO.cleanup()


    def open(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servopin, GPIO.OUT)
        pwm = GPIO.PWM(self.servopin, 50)
        pwm.start(0)
        try: 
            pwm.ChangeDutyCycle(5.0)
            time.sleep(1)
            pwm.stop()
        except KeyboardInterrupt:
            pwm.stop()
            GPIO.cleanup()

    def close(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servopin, GPIO.OUT)
        pwm = GPIO.PWM(self.servopin, 50)
        pwm.start(0)
        try: 
            pwm.ChangeDutyCycle(11.0)
            time.sleep(1)
            pwm.stop()
        except KeyboardInterrupt:
            pwm.stop()
            GPIO.cleanup()



