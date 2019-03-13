from piConfig import PI_INTERFACE_CONFIG
import gui
import time
import storage

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

# immediate dispense

# wait 5 minutes to see if the button was pressed
def pressed_button(gpio, win, button_colour, timeout):
    timeout_start = time.time()
    #print("Waiting for button press")
    while time.time() < timeout_start + timeout:
        if(gpio.input(PI_INTERFACE_CONFIG[button_colour]) == gpio.LOW):
            while time.time() < timeout_start + timeout:
                if(gpio.input(PI_INTERFACE_CONFIG[button_colour]) == gpio.HIGH):
                    time.sleep(0.5)
                    return True
                gui.maintain_gui(win)
        gui.maintain_gui(win)
    print("Timed out!")
    return False


def pressed_red_button(gpio, win, quadrant, pills_per_dose, kit):
    timeout_start = time.time()
    print("Waiting for button press")
    while time.time() < timeout_start + 3:
        if(gpio.input(PI_INTERFACE_CONFIG["red_button"]) == gpio.LOW):
            while time.time() < timeout_start + 3:
                if(gpio.input(PI_INTERFACE_CONFIG["red_button"]) == gpio.HIGH):
                    time.sleep(0.5)
                    storage.dispense(quadrant, pills_per_dose, kit, win, gpio)
                gui.maintain_gui(win)
        gui.maintain_gui(win)
    return False


def sound_buzzer(gpio):
    gpio.output(PI_INTERFACE_CONFIG["buzzer"], gpio.HIGH)
    time.sleep(0.5)
    gpio.output(PI_INTERFACE_CONFIG["buzzer"], gpio.LOW)

        

