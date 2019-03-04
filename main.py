import schedule
import time
import parse_json as parse_json

def main2():
    parse_json.main1()
    while True:
      schedule.run_pending()
      time.sleep(1)

main2()