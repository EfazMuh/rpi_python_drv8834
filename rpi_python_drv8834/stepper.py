import Jetson.GPIO as GPIO
from time import sleep

class StepperMotor:
    def __init__(self, step_pin, dir_pin, mode_pins, step_type):
        """docstring for ."""
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(step_pin, GPIO.OUT)
        GPIO.setup(dir_pin, GPIO.OUT)
        GPIO.setup(mode_pins, GPIO.OUT)
        resolution = {'Full':(0, 0),
                    'Half':(1, 0),
                    '1/4':(0, 0), # M0 must be disconnected
                    '1/8':(0, 1),
                    '1/16':(1, 1),
                    '1/32':(0, 1)} # M0 must be disconnected
        microsteps =  {'Full':1,
                    'Half':2,
                    '1/4':4,
                    '1/8':8,
                    '1/16':16,
                    '1/32':32}
        self.delay = .005/microsteps[step_type]
        GPIO.output(mode_pins, resolution[step_type])

    def run(self, steps, clockwise):
        GPIO.output(self.dir_pin, clockwise)
        for i in range(steps):
            GPIO.output(self.step_pin, GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(self.step_pin, GPIO.LOW)
            sleep(self.delay)
