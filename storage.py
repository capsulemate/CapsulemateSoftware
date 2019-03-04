# this class is so we can have objects for each of the storage containers with their associated servo_numbers ... ...
# Additional things to add once we are done MVP:
# -warning when pills are almost out, tell them to refill
import schedule
import time
from piConfig import PI_CONFIG


MAX_NUM_TRIES = 3
NUM_LOW_ON_PILLS = 10

class Storage:
  # add any other attributes you need, I feel like we need the num of pills and name of medicine to display to the screen
  # but we might want to create another class for displaying things to the screen
  def __init__(self, storage_container, med_name = "", num_pills = 0):
    self.storage_container = storage_container
    self.med_name = med_name
    self.num_pills = num_pills
    # get sensor pin numbers from Raspberry PI config
    self.servo_motor_top = PI_CONFIG[storage_container]["servo_motor_top"]
    self.servo_motor_cylinder = PI_CONFIG[storage_container]["servo_motor_cylinder"]
    self.solenoid = PI_CONFIG[storage_container]["solenoid"]
    self.photoresistor = PI_CONFIG[storage_container]["photoresistor"]
        
# ------------------METHODS -------------------------------------------------------------

def turn_cylinder(quadrant, hole_size):
  # actually turn the motor
  # print the below message to the screen
	print("Please fill storage container " + str(quadrant.storage_container) + " with medicine " + quadrant.med_name)
	# wait for them to press a button acknowledging they've filled the container before moving on 
 
def dispense(quadrant, pills_per_dose):
  # start stirring the stirring rod
  for i in range(pills_per_dose):
    num_tries = 0
    dispensed = dispense_single(quadrant)
    while not dispensed and num_tries < MAX_NUM_TRIES:
      dispensed = dispense_single(quadrant)
      num_tries = num_tries + 1
    if dispensed:
      # need to make num_pills a global variable or make a medicine class to keep count of pills
      quadrant.num_pills = quadrant.num_pills - pills_per_dose 
      if quadrant.num_pills < pills_per_dose:
        cancel_job()
      else:
       if quadrant.num_pills < NUM_LOW_ON_PILLS:
         low_on_pills()
       print(quadrant.med_name + " was dispensed")
       return True
        # print some other message that the pills were dispensed
        # sound the buzzer 
        # wait for button press for acknowledgement
        # print("Dispensed" + pills_per_dose + "pills")

def dispense_single(quadrant):
  # power the correct solenoid to push 
  return did_dispense(quadrant)

def did_dispense(quadrant):
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