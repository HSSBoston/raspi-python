import RPi.GPIO as GPIO
import time
from bluedot import BlueDot
GPIO.setmode(GPIO.BCM)
# Start writing your own program below
pins = [21, 25]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
bdot = BlueDot()

while True:
    try:
        bdot.wait_for_press()
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH)
        bdot.wait_for_press()
        for pin in pins:
            GPIO.output(pin, GPIO.LOW)     
        
    except KeyboardInterrupt:
        break
   
# Write your program above this line
GPIO.cleanup()



