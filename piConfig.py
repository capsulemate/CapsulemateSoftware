## Servo channel ID and GPIO constants
PI_DISPENSER_CONFIG = [
    {
        "servo_motor_top": 0,
        "servo_motor_cylinder": 8,
        "solenoid": 4,
        "photoresistor": 17
    },
    {
        "servo_motor_top": 2,
        "servo_motor_cylinder": 9,
        "solenoid": 18,
        "photoresistor": 27
    },
    {
        "servo_motor_top": 4,
        "servo_motor_cylinder": 10,
        "solenoid": 22,
        "photoresistor": 23
    },
    {
        "servo_motor_top": 6,
        "servo_motor_cylinder": 11,
        "solenoid": 24,
        "photoresistor": 25
    },
]

#Interface GPIO constants
PI_INTERFACE_CONFIG = {
    "red_button": 5,
    "yellow_button": 6,
    "green_button": 12,
    "buzzer": 13
}

## Hole 1 is Largest, hole 4 is smallest
PI_CYLINDER_CONFIG = [
    {
        "hole1": 170,
        "hole2": 115,
        "hole3": 65,
        "hole4": 0
    },
    {
        "hole1": 20,
        "hole2": 180,
        "hole3": 125,
        "hole4": 75
    },
    {
        "hole1": 105,
        "hole2": 50,
        "hole3": 0,
        "hole4": 160
    },
    {
        "hole1": 65,
        "hole2": 180,
        "hole3": 125,
        "hole4": 0
    },
]


