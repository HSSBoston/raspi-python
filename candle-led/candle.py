import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Start writing your own program below
pin = 21
sleep = 10
GPIO.setup(pin, GPIO.OUT)
    
for x in range (1):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(sleep)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(sleep)

# Write your program above this line
GPIO.cleanup()