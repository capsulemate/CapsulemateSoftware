import schedule
import time
import loading

def main():
    loading.load_pills()
    while True:
      schedule.run_pending()
      time.sleep(1)

main()