import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Start writing your own program below
blue = 21
sleep = 0.5
GPIO.setup(blue, GPIO.OUT)

GPIO.output(blue, GPIO.HIGH)
time.sleep(sleep)
GPIO.output(blue, GPIO.LOW)
time.sleep(sleep)
GPIO.output(blue, GPIO.HIGH)
time.sleep(sleep)
GPIO.output(blue, GPIO.LOW)
time.sleep(sleep)
GPIO.output(blue, GPIO.HIGH)
time.sleep(sleep)
GPIO.output(blue, GPIO.LOW)
time.sleep(sleep)
GPIO.output(blue, GPIO.HIGH)
time.sleep(sleep)
GPIO.output(blue, GPIO.LOW)
time.sleep(sleep)
# Write your program above this line
GPIO.cleanup()