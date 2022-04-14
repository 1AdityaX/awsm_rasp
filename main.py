from utility.utility import take_picture, classify_image
from utility.servo import Servo

classfication = classify_image()

servo1 = Servo(17)
servo2 = Servo(27)
top_servo = Servo(22)

if classfication == "plastic":
    servo1.left()
    servo2.left()

elif classfication == "metal":
    servo1.left()
    servo2.right()

elif classfication == "paper" or classfication == "cardboard":
    servo1.right()
    servo2.left()

else:
    servo1.right()
    servo2.right()

