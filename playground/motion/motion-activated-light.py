import RPi.GPIO as GPIO, time
from kintone import getCurrentTimeStamp
GPIO.setmode(GPIO.BCM)
# Start writing your program below

motionPin = 2
lightPin = 26
GPIO.setup(motionPin, GPIO.IN)
GPIO.setup(lightPin, GPIO.OUT)

lightOnDuration = 5
motionDetectionInterval = 5

while True:
    try:
        if GPIO.input(motionPin) == GPIO.HIGH:
            print("Motion detected: " + getCurrentTimeStamp())
            GPIO.output(lightPin, GPIO.HIGH)
            time.sleep(lightOnDuration)
            GPIO.output(lightPin, GPIO.LOW)
            time.sleep(motionDetectionInterval)
    except KeyboardInterrupt:
        break


# Write your program above this line
GPIO.cleanup()
