import RPi.GPIO as GPIO
import time
from piConfig import PI_INTERFACE_CONFIG
GPIO.setmode(GPIO.BCM)
GPIO.setup(PI_INTERFACE_CONFIG["red_button"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
while(True):
    time.sleep(0.05)
    print(GPIO.input(PI_INTERFACE_CONFIG["red_button"]))