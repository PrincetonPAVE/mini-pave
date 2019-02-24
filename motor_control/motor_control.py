import RPi.GPIO as GPIO
import time


MOTOR_CONTROL = 12 # pin 12 is 6th from the left on the outside

GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTOR_CONTROL, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWM(MOTOR_CONTROL, 100)
p.start(70)
input("lol")
p.stop()
GPIO.cleanup()
