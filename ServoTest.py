import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.continuous_servo[0].throttle = 0.25
kit.continuous_servo[2].throttle = 0.25
kit.continuous_servo[4].throttle = 0.25
kit.continuous_servo[6].throttle = 0.25

time.sleep(1.5)

kit.continuous_servo[0].throttle = -0.05
kit.continuous_servo[2].throttle = 0
kit.continuous_servo[4].throttle = 0
kit.continuous_servo[6].throttle = 0.05

def servoTest(chID):
    kit.servo[chID].angle = 0
    time.sleep(1)
    kit.servo[chID].angle = 65
    time.sleep(1)
    kit.servo[chID].angle = 115
    time.sleep(1)
    kit.servo[chID].angle = 170
    time.sleep(1)
    kit.servo[chID].angle = 0

##servoTest(8)
##servoTest(9)
