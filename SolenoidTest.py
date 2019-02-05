import RPi.GPIO as GPIO
import time
from adafruit_servokit import ServoKit

GPIO.setmode(GPIO.BCM)
solenoid1 = 27
GPIO.setup(solenoid1, GPIO.OUT)

kit = ServoKit(channels=16)
time.sleep(0.5)
kit.continuous_servo[15].throttle = -0.25

time.sleep(1.5)
def dispense ():
    GPIO.output(solenoid1, True)
    time.sleep(0.5)
    GPIO.output(solenoid1, False)
    time.sleep(1)

for i in range(10):
    dispense()

time.sleep(5)
kit.continuous_servo[15].throttle = 0.1

print('test done')


GPIO.cleanup()
