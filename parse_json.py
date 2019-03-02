import json
import schedule
import time

# -------------- function to rotate the cylinder to the correct hole size
def turn_cylinder(storage_container, medicine_name, hole_size):
  # actually turn the motor
  # print this message to the screen
	print("Please fill storage container " + str(storage_container) + " with medicine " + medicine_name)
	# wait for button press for them to fill the container before moving on 
	# if the storage container == 4 print an all done message

#------------ function to create the sechedule
def create_schedule(storage_container, medicine_name, dispense_times, pills_per_dose):
  for time in dispense_times:
    schedule.every().day.at(time).do(dispense)

# --------------- function for the actual dispensing
def dispense(storage_container, medicine_name, pills_per_dose):
  num_tries = 0
  for i in range(pills_per_dose):
    dispensed = dispense_single(storage_container, photoresistor_number)
    while not dispensed or num_tries < 3:
      dispensed = dispense_single(storage_container, photoresistor_number)
      num_tries = num_tries + 1
    


  print("Dispensed" + pills_per_dose + "pills")
	#sit the appropriate stirring rod
	#power the correct solenoid


# --------------- function to dispense a single pill so we can check that it "did_dipsense" in between
def dispense_single(storage_container, photoresistor_number):
  # dispense using the solenoid
  return did_dispense(storage_container, photoresistor_number)
  
# --------------function for the photoresistor to check
def did_dispense(storage_container, photoresistor_number, num_pills, pills_per_dose):
  #use bool to check the correct photosensor to see if it dispensed
  dispensed = False; 

    dispense(storage_container, pills_per_dose)
  num_pills = num_pills - pills_per_dose 
  if num_pills < pills_per_dose:
    schedule.cancel_job(self, dispense)
  # else: 
  return True 



def main1():
    with open('template.json') as template:
      data = json.load(template)["Medicine"]
      for med in data: 
        storage_container = med["StorageContainer"]
        medicine_name = med["Name"]
        hole_size = med["Size"]
        dispense_times = med["DispenseTimes"]
        pills_per_dose = med["PillsPerDose"]
        num_pills = med["NumPills"]
        turn_cylinder(storage_container, medicine_name, hole_size)
        create_schedule(storage_container, dispense_times, pills_per_dose)

def main2():
    	# all the code for polling
  while True:
      schedule.run_pending()
      time.sleep(1)

main1()
# main2()