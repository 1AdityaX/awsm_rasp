from utility.servo import Servo

servo1 = Servo(14)
servo2 = Servo(27)
top_servo = Servo(22)

servo1.right()
servo1.left()
servo1.middle()
servo2.right()
servo2.left()
servo2.middle()
top_servo.open()
top_servo.close()