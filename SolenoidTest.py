import RPi.GPIO as GPIO
import time
from adafruit_servokit import ServoKit

GPIO.setmode(GPIO.BCM)
solenoid1 = 18
servoID = 2

GPIO.setup(solenoid1, GPIO.OUT)

def dispense (solenoidGPIO):
    GPIO.output(solenoidGPIO, True)
    time.sleep(0.5)
    GPIO.output(solenoidGPIO, False)
    time.sleep(1)

kit = ServoKit(channels=16)
time.sleep(0.5)
kit.continuous_servo[servoID].throttle = -0.25
time.sleep(1.5)

for i in range(5):
    print('dispense')
    dispense(solenoid1)

time.sleep(1)
kit.continuous_servo[servoID].throttle = 0

print('test done')


GPIO.cleanup()























