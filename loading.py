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
def load_pills():
  # make objects for each of the storage quadrants
  quadrant = [Storage(0), Storage(1), Storage(2), Storage(3)]

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
      quadrant[current_quadrant].med_name = medicine_name
      quadrant[current_quadrant].num_pills = num_pills
        
      storage.turn_cylinder(quadrant[current_quadrant], hole_size)
      create_schedule(quadrant[current_quadrant], dispense_times, pills_per_dose)
      current_quadrant = current_quadrant + 1
  print("Loading process is done!")
        