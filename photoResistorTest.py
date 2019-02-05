import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)

def rctime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    while(GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

while True:
    print(rctime(18))
##    if rctime(18) > 8000:
##        print('PILL', rctime(18))
