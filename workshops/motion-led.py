import RPi.GPIO as GPIO, subprocess, sys, time, kintone, iotutils
from iotutils import getCurrentTimeStamp
GPIO.setmode(GPIO.BCM)
# Write your program below

motionPin = 21
GPIO.setup(motionPin, GPIO.IN)
ledPin = 20
GPIO.setup(ledPin, GPIO.OUT)
interval = 5
while True:
    try:
        if GPIO.input(motionPin) == GPIO.HIGH:
            print("Motion detected: " + getCurrentTimeStamp())
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(interval)
            GPIO.output(ledPin, GPIO.LOW)
    except KeyboardInterrupt:
        break
# Write your program above this line
GPIO.cleanup()
