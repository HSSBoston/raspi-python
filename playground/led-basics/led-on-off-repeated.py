import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Start writing your own program below

GPIO.setup(21, GPIO.OUT)

GPIO.output(21, GPIO.HIGH)
time.sleep(3)
GPIO.output(21, GPIO.LOW)
time.sleep(1)
GPIO.output(21, GPIO.HIGH)
time.sleep(3)
GPIO.output(21, GPIO.LOW)
time.sleep(1)
GPIO.output(21, GPIO.HIGH)
time.sleep(3)
GPIO.output(21, GPIO.LOW)
time.sleep(1)
GPIO.output(21, GPIO.HIGH)
time.sleep(3)
GPIO.output(21, GPIO.LOW)
time.sleep(1)
# Write your program above this line
GPIO.cleanup()