from piConfig import PI_INTERFACE_CONFIG
import gui
import time

## return any of 3 buttons that are pressed
def wait_for_button_press(gpio, win):
    while(True):
        # if(gpio.input(PI_INTERFACE_CONFIG["red_button"]) == gpio.LOW):
        #     return "red_button"
        # if(gpio.input(PI_INTERFACE_CONFIG["yellow_button"]) == gpio.LOW):
        #     return "yellow_button"
        if(gpio.input(PI_INTERFACE_CONFIG["green_button"]) == gpio.LOW):
            while(True):
                # if(gpio.input(PI_INTERFACE_CONFIG["red_button"]) == gpio.LOW):
                #     return "red_button"
                # if(gpio.input(PI_INTERFACE_CONFIG["yellow_button"]) == gpio.LOW):
                #     return "yellow_button"
                if(gpio.input(PI_INTERFACE_CONFIG["green_button"]) == gpio.HIGH):
                    return
                gui.maintain_gui(win)
        gui.maintain_gui(win)
        

