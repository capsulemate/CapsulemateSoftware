import schedule
import time
import loading
import piConfig

def main():
    loading.load_pills()
    piConfig.init_sensors()
    while True:
      schedule.run_pending()
      time.sleep(1)

main()