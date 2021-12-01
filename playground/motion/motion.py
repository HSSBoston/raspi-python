import RPi.GPIO as GPIO, os, sys, kintone, time
from kintone import getCurrentTimeStamp
GPIO.setmode(GPIO.BCM)
# Start writing your program below

motionPin = 21
GPIO.setup(motionPin, GPIO.IN)
interval = 5

while True:
    try:
        if GPIO.input(motionPin) == GPIO.HIGH:
            print("Motion detected: " + getCurrentTimeStamp())
            time.sleep(interval)
    except KeyboardInterrupt:
        break


# Write your program above this line
GPIO.cleanup()
