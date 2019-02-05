import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


kit.servo[4].actuation_range = 180

kit.servo[4].angle = 0

time.sleep(1)

kit.servo[4].angle = 45

time.sleep(1)

kit.servo[4].angle = 90

time.sleep(1)

kit.servo[4].angle = 135

time.sleep(1)

kit.servo[4].angle = 180

time.sleep(1)

kit.servo[4].angle = 90

time.sleep(1)

kit.servo[4].angle = 0

