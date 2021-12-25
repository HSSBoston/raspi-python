import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Start writing your program below

star = 12
GPIO.setup(star, GPIO.OUT)
interval = 3

GPIO.output(star, GPIO.HIGH)
time.sleep(interval)
GPIO.output(star, GPIO.LOW)

# Write your program above this line
GPIO.cleanup()