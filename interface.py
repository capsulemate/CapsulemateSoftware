from piConfig import PI_INTERFACE_CONFIG
import gui
import time

## return any of 3 buttons that are pressed
def wait_for_button_press(gpio, win, button_colour):
    while(True):
        if(gpio.input(PI_INTERFACE_CONFIG[button_colour]) == gpio.LOW):
            while(True):
                if(gpio.input(PI_INTERFACE_CONFIG[button_colour]) == gpio.HIGH):
                    time.sleep(0.5)
                    return
                gui.maintain_gui(win)
        gui.maintain_gui(win)


# wait 5 minutes to see if the button was pressed
def pressed_button(gpio, win, button_colour, timeout):
    timeout_start = time.time()
    print("Waiting for button press")
    while time.time() < timeout_start + timeout:
        wait_for_button_press(gpio, win, button_colour)
        return True
    print("Timed out!")
    return False

def sound_buzzer(gpio):
    gpio.output(PI_INTERFACE_CONFIG["buzzer"], gpio.HIGH)
    time.sleep(0.5)
    gpio.output(PI_INTERFACE_CONFIG["buzzer"], gpio.LOW)

        

