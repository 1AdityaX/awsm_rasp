import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM) 

trig = 17
echo = 27

GPIO.setup(trig, GPIO.OUT) 
GPIO.setup(echo, GPIO.IN) 
GPIO.output(trig, 1) 

time.sleep(2) 

def func():
    GPIO.output(trig, 1) 

    time.sleep(1) 

    GPIO.output(trig, 0) 

    while GPIO.input(echo)==0: 
        start_time = time.time() 

    while GPIO.input(echo)==1: 
        Bounce_back_time = time.time() 
    
    pulse_duration = Bounce_back_time - start_time 
    distance = round(pulse_duration * 17150, 2) 
    return distance


try:
    while True:
        distance = func()
        print (f"Distance: {distance} cm") 
except KeyboardInterrupt:
    GPIO.cleanup() 




