import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#Write your program below

GPIO.setup(21, GPIO.OUT)

for x in range(5):
    GPIO.output(21, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(21, GPIO.LOW)
    time.sleep(2)

# Write your program above
GPIO.cleanup()
# DO NOT write your program below