import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Start writing your own program below
pins = [21, 20, 16, 12, 7, 8, 25, 24]
sleep = 0.1
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    
for x in range (10):
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(sleep)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(sleep)

# Write your program above this line
GPIO.cleanup()