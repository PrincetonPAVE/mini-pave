import RPi.GPIO as GPIO
import time
import math

pin = 16 # pin 12 is 6th from the left on the outside

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 50)

print ("\nPress Ctl C to quit \n")

dc = 1
pwm.start(dc)

counter = 0

try:
    while True:
        time.sleep(0.01)
        counter += 0.01
        
        dc = (1.5+(math.sin(counter)/2))*5
        
        print("dc: {}".format(dc))
        pwm.ChangeDutyCycle(dc)

except KeyboardInterrupt:
    print("Ctl C pressed. Stopping.")
   
pwm.stop()
GPIO.cleanup()


