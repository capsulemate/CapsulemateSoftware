# this class is so we can have objects for each of the storage containers with their associated servo_numbers ... ...
import schedule
import time
import gui
import interface
import external
import datetime
from piConfig import PI_DISPENSER_CONFIG, PI_CYLINDER_CONFIG 

TOP_SERVO_SPEED = 0.25
MAX_NUM_TRIES = 10
NUM_LOW_ON_PILLS = 10
PHOTOSENSOR_THRESHOLD = [250, 200, 250, 290]

class Storage:
  # add any other attributes you need, I feel like we need the num of pills and name of medicine to display to the screen
  # but we might want to create another class for displaying things to the screen
  def __init__(self, storage_container, gpio, med_name = "", num_pills = 0):
    self.storage_container = storage_container
    self.med_name = med_name
    self.num_pills = num_pills
    # get sensor pin numbers from Raspberry PI config
    self.servo_motor_top = PI_DISPENSER_CONFIG[storage_container]["servo_motor_top"]
    self.servo_motor_cylinder = PI_DISPENSER_CONFIG[storage_container]["servo_motor_cylinder"]
    self.solenoid = PI_DISPENSER_CONFIG[storage_container]["solenoid"]
    self.photoresistor = PI_DISPENSER_CONFIG[storage_container]["photoresistor"]
    gpio.setup(self.solenoid, gpio.OUT)
    
        
# ------------------METHODS -------------------------------------------------------------

def turn_cylinder(quadrant, hole_size, kit):
  # actually turn the motor
  kit.servo[quadrant.servo_motor_cylinder].angle = PI_CYLINDER_CONFIG[quadrant.storage_container]["hole{}".format(hole_size)]
 
def dispense(quadrant, pills_per_dose, kit, win, gpio):
  # start stirring the stirring rod
  kit.continuous_servo[quadrant.servo_motor_top].throttle = TOP_SERVO_SPEED
  time.sleep(5)
  for i in range(pills_per_dose):
    num_tries = 0
    pill_present = is_pill_present(quadrant, gpio)
    while not pill_present and num_tries < MAX_NUM_TRIES:
      time.sleep(1) # give extra 2 seconds to blend
      num_tries = num_tries + 1
      pill_present = is_pill_present(quadrant, gpio)
    if pill_present:
      dispense_single(quadrant, gpio)
      quadrant.num_pills = quadrant.num_pills - pills_per_dose 
      if quadrant.num_pills < pills_per_dose:
        cancel_job()
      else:
       if quadrant.num_pills < NUM_LOW_ON_PILLS:
           gui.change_instruction_text(win, " Medicine {} is running low, please refill".format(quadrant.med_name))
           time.sleep(1)
    else:
       gui.change_instruction_text(win, "Photoresistor does not detect in quadrant {}".format(quadrant.storage_container))   
  gui.change_instruction_text(win, "Dispensed {}...".format(quadrant.med_name))
  kit.continuous_servo[quadrant.servo_motor_top].throttle = 0
  buzz(gpio)
  acknowledgement(gpio, win, quadrant)

def storage_test(win):
      gui.change_instruction_text(win, "Next pill will be dispensed at {}".format(schedule.next_run()))

def acknowledgement(gpio, win, quadrant):
      # wait 5 min (300 seconds) for a button press
      if interface.pressed_button(gpio, win, "yellow_button", 10):
        gui.change_instruction_text(win, "Next pill will be dispensed at {}".format(schedule.next_run()))
      else:
        print("We are sending")
        external.sendemail(['tyurina.kumar@gmail.com'], quadrant.med_name)
        gui.change_instruction_text(win, "Contacted caregiver")

def buzz(gpio):
    next_dispense = schedule.next_run()
    current_time = datetime.datetime.now()
    now = current_time.replace(second=0, microsecond=0)
    diff = next_dispense - now
    five_min = datetime.timedelta(minutes=5)
    if (next_dispense - now > five_min):
      interface.sound_buzzer(gpio)
    else: 
      pass

def dispense_single(quadrant, gpio):
  # power the correct solenoid to push
  gpio.output(quadrant.solenoid, True)
  time.sleep(0.5)
  gpio.output(quadrant.solenoid, False)
  time.sleep(1)
  print("dispensed")
  return 

def is_pill_present(quadrant, gpio):
  # check if the photoresistor detected anything and return true or false
  print("checking photoresistor")
  samples = [0]*10
  for i in range(10):
        samples[i] = photosensor_read(quadrant.photoresistor, gpio)
  avg = sum(samples) / 10
  print("avg = {}".format(avg))
  for s in samples:
      print("sample = {}".format(s))
  if avg > PHOTOSENSOR_THRESHOLD[quadrant.storage_container]:
        return True
  return False

def photosensor_read(RCpin, gpio):
    reading = 0
    gpio.setup(RCpin, gpio.OUT)
    gpio.output(RCpin, gpio.LOW)
    time.sleep(0.1)

    gpio.setup(RCpin, gpio.IN)
    while(gpio.input(RCpin) == gpio.LOW):
        reading += 1
    return reading

def cancel_job():
  schedule.CancelJob()
  