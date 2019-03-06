from piConfig import PI_INTERFACE_CONFIG
import gui

## return any of 3 buttons that are pressed
def wait_for_button_press(gpio, win):
    while(True):
        # if(gpio.input(PI_INTERFACE_CONFIG["red_button"]) == gpio.LOW):
        #     return "red_button"
        # if(gpio.input(PI_INTERFACE_CONFIG["yellow_button"]) == gpio.LOW):
        #     return "yellow_button"
        if(gpio.input(PI_INTERFACE_CONFIG["green_button"]) == gpio.LOW):
            return "green_button"
        gui.maintain_gui(win)    

