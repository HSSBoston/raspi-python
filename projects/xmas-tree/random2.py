import RPi.GPIO as GPIO
import time, random
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

greenLeds = [bottomLeft, bottomMidRight, middleMidLeft, middleRight, topRight]
redLeds = [bottomMidLeft, bottomRight, middleLeft, middleMidRight, topLeft]

GPIO.setup(allLeds, GPIO.OUT)

GPIO.output(star, GPIO.HIGH)
while True:
    try:
        bottom = random.choice(bottomLeds)
        middle = random.choice(middleLeds)
        top = random.choice(topLeds)
        GPIO.output(bottom, GPIO.HIGH)
        GPIO.output(middle, GPIO.HIGH)
        GPIO.output(top, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(bottom, GPIO.LOW)
        GPIO.output(middle, GPIO.LOW)
        GPIO.output(top, GPIO.LOW)
    except KeyboardInterrupt:
        break

GPIO.output(allLeds, GPIO.LOW)

# Write your program above this line
GPIO.cleanup()