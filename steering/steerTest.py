import RPi.GPIO as GPIO
import time

pin = 16 # pin 16 is 8th from the left on the outside

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)

print ("\nPress Ctl C to quit \n")

servoPositions = [-40, -20, 0, 20, 40]
servoOffset = 20

def setServoPosition(angle, duration):
    delay_between_signals = .040
    delay = 0.0015 + 0.0005 * ((angle + servoOffset) / 90)
    total_cycles = int(duration / (delay + delay_between_signals))
    for i in range(total_cycles):
        GPIO.output(pin, 1)
        time.sleep(delay)
        GPIO.output(pin,0)
        time.sleep(delay_between_signals)

try:
    while True:
        for pos in servoPositions:
            print('Setting servo pos: ' + str(pos))
            setServoPosition(pos, 2)
        
except KeyboardInterrupt:
    print("Ctl C pressed. Stopping.")
    
GPIO.cleanup()


