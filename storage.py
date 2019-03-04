# this class is so we can have objects for each of the storage containers with their associated servo_numbers ... ...
# Additional things to add once we are done MVP:
  # -warning when pills are almost out, tell them to refill
import schedule
import time

class Storage:
  # add any other attributes you need, I feel like we need the num of pills and name of medicine to display to the screen
  # but we might want to create another class for displaying things to the screen
  def __init__(self, storage_container,servo_motor_top, servo_motor_cylinder,solenoid, photoresistor, med_name, num_pills):
    self.storage_container = storage_container
    self.servo_motor_top = servo_motor_top
    self.servo_motor_cylinder = servo_motor_cylinder
    self.solenoid = solenoid
    self.photoresistor = photoresistor
    self.med_name = med_name
    self.num_pills = num_pills
        
# ------------------METHODS -------------------------------------------------------------

def turn_cylinder(storage_container, medicine_name, hole_size):
  # actually turn the motor
  # print the below message to the screen
	print("Please fill storage container " + str(storage_container) + " with medicine " + medicine_name)
	# wait for them to press a button acknowledging they've filled the container before moving on 
	# if the storage container == 4 print an all done message
 
def dispense(storage_container, medicine_name, pills_per_dose, photoresistor):
  num_tries = 0
  # start stirring the stirring rod
  for i in range(pills_per_dose):
    dispensed = dispense_single(storage_container, photoresistor)
    while not dispensed and num_tries < 3:
      dispensed = dispense_single(storage_container, photoresistor)
      num_tries = num_tries + 1
    if dispensed:
      # need to make num_pills a global variable or make a medicine class to keep count of pills
      num_pills = num_pills - pills_per_dose 
      if num_pills < pills_per_dose:
        cancel_job()
      else:
       return True
        # print some other message that the pills were dispensed
        # sound the buzzer 
        # wait for button press for acknowledgement
        # print("Dispensed" + pills_per_dose + "pills")


def dispense_single(storage_container, photoresistor_number):
  # power the correct solenoid to push 
  return did_dispense(storage_container, photoresistor_number)

def did_dispense(storage_container, photoresistor_number):
  # check if the photoresistor detected anything and return true or false
  # use an averaging function over the course of 2 seconds 
  dispensed = False
  return dispensed

def cancel_job(): 
  # finish this function
  # consult https://github.com/dbader/schedule/ for correct syntax for cancelling a job
    schedule.CancelJob
  # print message to screen that there is not enough pills

def low_on_pills(): 
  # function that warns when their is less than 10 pills
  return True