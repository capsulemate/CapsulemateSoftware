##KILL ALL
import RPi.GPIO as GPIO
import time
from piConfig import PI_DISPENSER_CONFIG
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.continuous_servo[0].throttle = 0.0
kit.continuous_servo[2].throttle = 0.05
kit.continuous_servo[4].throttle = 0.05
kit.continuous_servo[6].throttle = 0

GPIO.setmode(GPIO.BCM)
for i in range(4):
    GPIO.setup(PI_DISPENSER_CONFIG[i]["solenoid"], GPIO.OUT)
    GPIO.output(PI_DISPENSER_CONFIG[i]["solenoid"], False)