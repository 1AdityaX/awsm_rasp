from utility.servo import Servo

servo1 = Servo(5)
servo2 = Servo(6)
top_servo = Servo(13)

servo1.right()
servo1.left()
servo1.middle()
servo2.right()
servo2.left()
servo2.middle()
top_servo.open()
top_servo.close()