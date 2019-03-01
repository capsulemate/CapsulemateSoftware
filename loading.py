import json
import schedule
import time
import storage
from storage import Storage


#------------ function to create the sechedule
def create_schedule(quadrant, dispense_times, pills_per_dose):
  for time in dispense_times:
    schedule.every().day.at(time).do(storage.dispense, quadrant, pills_per_dose)

# ----------------------------- start of main
def load_pills(win):
  # make objects for each of the storage quadrants
  quadrants = [Storage(0), Storage(1), Storage(2), Storage(3)]

  current_quadrant = 0
  with open('template.json') as template:
    data = json.load(template)["Medicine"]
    for med in data: 
      storage_container = med["StorageContainer"]
      medicine_name = med["Name"]
      hole_size = med["Size"]
      dispense_times = med["DispenseTimes"]
      pills_per_dose = med["PillsPerDose"]
      num_pills = med["NumPills"]
      # set medication information for corresponding Storage class
      quadrants[current_quadrant].med_name = medicine_name
      quadrants[current_quadrant].num_pills = num_pills
      # turn cylinder component to correct hole + get confirmation from user that the pills are in 
      storage.turn_cylinder(quadrants[current_quadrant], hole_size, win)
      create_schedule(quadrants[current_quadrant], dispense_times, pills_per_dose)
      current_quadrant = current_quadrant + 1
      time.sleep(5) #remove this once cylinder code is in
  print("Loading process is done!")
  return quadrants      