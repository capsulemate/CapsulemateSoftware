import csv
#from crontab import CronTab

# TODO: function to rotate the cylinder to the correct hole size
def turn_cylinder(storage_container, medicine_name, hole_size):
  # actually turn the motor
  # print this message to the screen
	print("Please fill storage container " + str(storage_container) + " with medicine" + medicine_name)
	# wait for button press for them to fill the container before moving on 
	# if the storage container == 4 print an all done message

# function for the actual dispensing
def dispense(storage_container):
	#sit the appropriate stirring rod
	#power the correct solenoid
	return True

# function for the photoresistor to check
def did_dispense(storage_container, photoresistor_number):
	# photoresistor code
	# output true or false
	return True 

def create_schedule(storage_container, dispense_time):
	return True

def main1():
	with open('template.txt') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter='|')
		line_count = 0
		total_medication = 0
		hole_size = 0
		for row in csv_reader:
			if line_count == 0:
				headers = row
				print(headers)
				line_count += 1
			else:
				storage_container = row[0]
				medicine_name = row[1]
				hole_size = row[2]
				dispense_time = row[4]
				turn_cylinder(storage_container, medicine_name, hole_size)
				create_schedule(storage_container, dispense_time)
				line_count += 1
				total_medication += 1

def main2():
    	# all the code for polling
    	return True


main1()
main2()