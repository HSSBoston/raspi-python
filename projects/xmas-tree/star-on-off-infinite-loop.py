import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Start writing your program below

star = 12
GPIO.setup(star, GPIO.OUT)
interval = 1

while True:
    try:
        GPIO.output(star, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(star, GPIO.LOW)
        time.sleep(interval)
    except KeyboardInterrupt:
        break

# Write your program above this line
GPIO.cleanup()