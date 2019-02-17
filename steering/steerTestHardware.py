import RPi.GPIO as GPIO
import time

pin = 12 # pin 12 is 6th from the left on the outside

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 10)

print ("\nPress Ctl C to quit \n")

dc = 1.4
pwm.start(dc)

try:
    while True:
      pass
        
except KeyboardInterrupt:
    print("Ctl C pressed. Stopping.")
   
pwm.stop()
GPIO.cleanup()


