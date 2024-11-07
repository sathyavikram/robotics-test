# from gpiozero import Servo
# from time import sleep
# from gpiozero.tools import sin_values
# from signal import pause

# servo = Servo(17)

# # while True:
# #     servo.min()
# #     sleep(2)
# #     servo.mid()
# #     sleep(2)
# #     servo.max()
# #     sleep(2)

# servo.source = sin_values()
# servo.source_delay = 0.1
# pause()

from gpiozero import AngularServo
from time import sleep

servo = AngularServo(17, min_angle=-90, max_angle=90)

while True:
    servo.angle = -90
    sleep(2)
    servo.angle = 0
    sleep(2)
    servo.angle = 90
    sleep(2)
