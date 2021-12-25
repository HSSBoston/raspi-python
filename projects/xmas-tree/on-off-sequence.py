import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Start writing your program below

bottomLeft, bottomMidLeft, bottomMidRight, bottomRight = (11, 16, 17, 18)
middleLeft, middleMidLeft, middleMidRight, middleRight =(19, 20, 21, 22)
topLeft, topRight =(23, 24)
star = 12

bottomLeds = [bottomLeft, bottomMidLeft, bottomMidRight, bottomRight]
middleLeds = [middleLeft, middleMidLeft, middleMidRight, middleRight]
topLeds = [topLeft, topRight]
allLeds = bottomLeds + middleLeds + topLeds + [star]

GPIO.setup(allLeds, GPIO.OUT)
interval = 1

for led in allLeds:
    GPIO.output(led, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(led, GPIO.LOW)

# Write your program above this line
GPIO.cleanup()