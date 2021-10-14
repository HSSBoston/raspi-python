import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
# Start writing your program below

redPins = [21, 20, 16, 12]
bluePins = [17, 27, 22, 10]
allPins = redPins + bluePins

for pin in allPins:
    GPIO.setup(pin, GPIO.OUT) 

while True:
    try:
        pin = random.choice(allPins)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(random.random()/10)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(random.random()/10)

    except KeyboardInterrupt:
        break


# Write your program above this line
GPIO.cleanup()
