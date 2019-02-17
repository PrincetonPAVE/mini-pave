import RPi.GPIO as GPIO
import time


MOTOR_CONTROL = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTOR_CONTROL, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWM(MOTOR_CONTROL, 20)
p.start(20)
input("lol")
p.stop()
GPIO.cleanup()
