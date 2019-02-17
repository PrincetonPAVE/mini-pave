import RPi.GPIO as GPIO
import time

pin = 12 # pin 12 is 6th from the left on the outside

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)

print ("\nPress Ctl C to quit \n")

try:
    while True:
        GPIO.output(pin, 1)
        
        time.sleep(.0015)
        
        GPIO.output(pin,0)
        
        time.sleep(.04)
        
except KeyboardInterrupt:
    print("Ctl C pressed. Stopping.")
    
GPIO.cleanup()


