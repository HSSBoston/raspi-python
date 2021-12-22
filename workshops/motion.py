import RPi.GPIO as GPIO, subprocess, sys, time, kintone, iotutils
from iotutils import getCurrentTimeStamp
GPIO.setmode(GPIO.BCM)
# Write your program below

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
