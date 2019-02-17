import RPi.GPIO as GPIO
import time


MOTOR_CONTROL = 12

GPIO.setmode(GPIO.BOARD
GPIO.setup(MOTOR_CONTROL, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        GPIO.output(MOTOR_CONTROL, GPIO.HIGH)
        time.sleep(1)
finally:
    GPIO.cleanup()
