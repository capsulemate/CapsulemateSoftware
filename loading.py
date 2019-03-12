import json
import schedule
import time
import storage
import gui
import interface
from storage import Storage


#------------ function to create the sechedule
def create_schedule(quadrant, dispense_times, pills_per_dose, kit, win, gpio):
  for time in dispense_times:
    schedule.every().day.at(time).do(storage.dispense, quadrant, pills_per_dose, kit, win, gpio)

# ----------------------------- start of main
def load_pills(win, gpio, kit):
  # make objects for each of the storage quadrants
  quadrants = [
    Storage(0, gpio),
    Storage(1, gpio), 
    Storage(2, gpio), 
    Storage(3, gpio)
  ]

  with open('templateTest.json') as template:
    data = json.load(template)["Medicine"]
    for med in data: 
      storage_container = med["StorageContainer"]
      medicine_name = med["Name"]
      hole_size = med["Size"]
      dispense_times = med["DispenseTimes"]
      pills_per_dose = med["PillsPerDose"]
      num_pills = med["NumPills"]
      # set medication information for corresponding Storage class
      quadrants[storage_container].med_name = medicine_name
      quadrants[storage_container].num_pills = num_pills
      # turn cylinder component to correct hole + get confirmation from user that the pills are in 
      storage.turn_cylinder(quadrants[storage_container], hole_size, kit)
      gui.change_instruction_text(win, "Please fill storage container {} with medicine {}".format(storage_container, medicine_name))
      gui.change_button_text(win, ["", "", "OK"])
      print("waiting for button" + medicine_name)
      interface.wait_for_button_press(gpio,win,"green_button") 
      create_schedule(quadrants[storage_container], dispense_times, pills_per_dose, kit, win, gpio)
  # loading done
  gui.change_instruction_text(win, "Loading Complete!")

  gui.change_button_text(win, ["", "", ""])
  time.sleep(3)
  storage.next_run(win)
  return quadrants      
