import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Start writing your program below

star = 12
GPIO.setup(star, GPIO.OUT)
interval = 1

for x in range(5):
    GPIO.output(star, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(star, GPIO.LOW)
    time.sleep(interval)

# Write your program above this line
GPIO.cleanup()