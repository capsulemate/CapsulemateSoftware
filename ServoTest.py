import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

##kit.continuous_servo[0].throttle = -0.25
##kit.continuous_servo[1].throttle = -0.25
##kit.continuous_servo[2].throttle = -0.25
##kit.continuous_servo[3].throttle = -0.25
##
##time.sleep(1.5)
##
##kit.continuous_servo[0].throttle = 0
##kit.continuous_servo[1].throttle = 0
##kit.continuous_servo[2].throttle = 0
##kit.continuous_servo[3].throttle = 0

def servoTest(chID):
    kit.servo[chID].angle = 0
    time.sleep(1)
    kit.servo[chID].angle = 45
    time.sleep(1)
    kit.servo[chID].angle = 90
    time.sleep(1)
    kit.servo[chID].angle = 135
    time.sleep(1)
    kit.servo[chID].angle = 180
    time.sleep(1)
    kit.servo[chID].angle = 110
    time.sleep(1)
##    kit.servo[chID].angle = 0

##servoTest(8)
servoTest(11)
