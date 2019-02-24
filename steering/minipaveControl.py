import RPi.GPIO as GPIO
import time
import math
import atexit
  
pin = 16 # pin 12 is 6th from the left on the outside

steering_angle = 0

pwm = GPIO.PWM(pin, 10)
pwm.start(get_duty_cycle())

def get_duty_cycle():
    return 1.5 + (get_steering_angld()/2)

def get_steering_angle():
    return steering_angle

def set_steering_angld(new_steering_angle):
    steering_angle = new_steering_angle
    pwm.ChangeDutyCycle(get_duty_cycle)


@atexit.register
def goodbye():
    pwm.stop()
    GPIO.cleanup()


GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

