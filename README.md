# CapsulemateSoftware
Control scripts to dispense pills and access prescription data

**TODO**:
- [ ] add  code to actually move the servos, solenoid (there are comments in storage.py corresponding to where these things should be added) 
- [ ] figure out how to execute two dispenses at once 
- [ ] add function to reset everything
- [ ] add function to dispense when a button is pressed "emergency dispense"
- [ ] add function to alert a caregiver if something is off i.e. they haven't taken their medicine
- [ ] put together a demo script (i.e add a medicine template)


Hardware Mapping:
Servo Channels
* Stirring  0, 2, 4, 6
* Cylinder  8 to 11


GPIO
* Dispenser 1 (Grey):
    * Solenoid: #4
    * Photoresistor: #17
* Dispenser 2:
    * Solenoid: #18
    * Photoresistor: #27
* Dispenser 3:
    * Solenoid: #22
    * Photoresistor: #23
* Dispenser 4:
    * Solenoid: #24
    * Photoresistor: #25


* Buttons:
    * Red: #5
    * Yellow: #6
    * Green: #12


* Buzzer: #13

