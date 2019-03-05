import schedule
import time
import loading
import gui
import piConfig

def main():

    win = gui.init_gui()
    quadrants = loading.load_pills(win)
    piConfig.init_sensors()
    while True:
      schedule.run_pending()
      time.sleep(1)
      # need to run this every loop iteration
      gui.maintain_gui(win)
    


main()
