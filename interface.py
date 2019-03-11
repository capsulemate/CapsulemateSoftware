from piConfig import PI_INTERFACE_CONFIG
import gui
import time
from gpiozero import Buzzer

## return any of 3 buttons that are pressed
def wait_for_button_press(gpio, win, button_colour):
    while(True):
        if(gpio.input(PI_INTERFACE_CONFIG[button_colour]) == gpio.LOW):
            while(True):
                if(gpio.input(PI_INTERFACE_CONFIG[button_colour]) == gpio.HIGH):
                    return
                gui.maintain_gui(win)
        gui.maintain_gui(win)


# wait 5 minutes to see if the button was pressed
def pressed_button(gpio, win, button_colour, timeout = 300):
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        wait_for_button_press(gpio, win, button_colour)
        return True
    return False

def sound_buzzer():
    buzzer = Buzzer(PI_INTERFACE_CONFIG["buzzer"])
    buzzer.on()
    time.sleep(0.5)
    buzzer.off()
    time.sleep(1)
        

