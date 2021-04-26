from stepper import StepperMotor
from time import sleep

# GPIO setup
step_pin = 23
dir_pin = 24
mode_pins = (14, 15)

# Stepper motor setup
step_type = '1/16'

# create object
motor = StepperMotor(step_pin, dir_pin, mode_pins, step_type)

motor.run(6400, True)     # run motor 6400 steps clowckwise
sleep(0.5)
motor.run(6400, False)    # run motor 6400 steps counterclockwise
