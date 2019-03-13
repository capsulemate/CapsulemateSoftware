## Buzzer Button Test
import time
import RPi.GPIO as GPIO
from piConfig import PI_INTERFACE_CONFIG


GPIO.setmode(GPIO.BCM)
GPIO.setup(PI_INTERFACE_CONFIG["buzzer"], GPIO.OUT)
GPIO.output(PI_INTERFACE_CONFIG["buzzer"], GPIO.HIGH)
time.sleep(0.5)
GPIO.output(PI_INTERFACE_CONFIG["buzzer"], GPIO.LOW)
GPIO.cleanup()




