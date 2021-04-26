# Raspberry Pi DRV8834 Python library 
Python Library to control a stepper motor with a DRV8834 driver connected to a Raspberry Pi

### How to use

###### 1. import library

```
from rpi_python_drv8834.stepper import StepperMotor
```

###### 2. create object

```
motor = StepperMotor(step_pin, dir_pin, mode_pins, step_type)
```

###### 3. run motor

```
motor.run(6400, True)     # run motor 6400 steps clowckwise
motor.run(6400, False)    # run motor 6400 steps counterclockwise
```

###### 4. note

To use microstep modes of 1/4 or 1/32, M0 must be left floating by disconnecting it from the GPIO pin.