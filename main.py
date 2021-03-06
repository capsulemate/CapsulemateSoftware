import schedule
import time
import loading
import gui
from piConfig import PI_INTERFACE_CONFIG
import external
import interface
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit

# code to initialize the servos, GPIO, Button, and Buzzer
# Solenoid is initialized in the storage class
def init_hardware():
      kit = ServoKit(channels=16)
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(PI_INTERFACE_CONFIG["red_button"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
      GPIO.setup(PI_INTERFACE_CONFIG["yellow_button"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
      GPIO.setup(PI_INTERFACE_CONFIG["green_button"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
      GPIO.setup(PI_INTERFACE_CONFIG["buzzer"], GPIO.OUT)
      print("Hardware initialized")
      return GPIO, kit

def main():

    win = gui.init_gui()
    gpio, kit = init_hardware()
    quadrants = loading.load_pills(win, gpio, kit)
#     external.sendemail("tyurina.kumar@gmail.com", "Tylenol")
    while True:
      schedule.run_pending()
      gui.change_instruction_text(win, "Next pill will be dispensed at {}".format(schedule.next_run()))
      gui.change_button_text(win, ["Dispense", "", ""])
      interface.pressed_red_button(gpio, win, quadrants[0], 1, kit)
      # need to run this every loop iteration
      gui.maintain_gui(win)
    


main()
