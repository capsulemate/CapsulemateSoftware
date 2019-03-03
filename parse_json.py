import json
import schedule
import time
import storage 


#------------ function to create the sechedule
def create_schedule(storage_container, medicine_name, dispense_times, pills_per_dose):
  for time in dispense_times:
    schedule.every().day.at(time).do(storage.dispense)

# ----------------------------- start of main
def main1():
  # make objects for each of the storage quadrants
  # quadrant_1 = storage()
  # quadrant_2 = storage()
  # quadrant_3 = storage()
  # quadrant_4 = storage()

  with open('template.json') as template:
    data = json.load(template)["Medicine"]
    for med in data: 
      storage_container = med["StorageContainer"]
      medicine_name = med["Name"]
      hole_size = med["Size"]
      dispense_times = med["DispenseTimes"]
      pills_per_dose = med["PillsPerDose"]
      num_pills = med["NumPills"]
      storage.turn_cylinder(storage_container, medicine_name, hole_size)
      create_schedule(storage_container, medicine_name, dispense_times, pills_per_dose)

#----------------------------- the code for running the schedule
# the scheduling code should run in background threads so that the program doesn't hang
def main2():
  while True:
      schedule.run_pending()
      time.sleep(1)

main1()
main2()