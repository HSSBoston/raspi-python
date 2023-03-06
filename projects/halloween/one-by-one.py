import RPi.GPIO as GPIO, time
GPIO.setmode(GPIO.BCM)
# Start writing your program below

leftBottom, leftMidBottom, leftMiddle, leftMidTop, leftTop = (18, 17, 16, 13, 24)
rightBottom, rightMidBottom, rightMiddle, rightMidTop, rightTop = (19, 20, 21, 22, 23)
leftEye, rightEye = (12, 6)

left =[leftBottom, leftMidBottom, leftMiddle, leftMidTop, leftTop]
right = [rightBottom, rightMidBottom, rightMiddle, rightMidTop, rightTop]
eyes = [leftEye, rightEye]
leftRight = left + right
all = left + right + eyes

GPIO.setup(all, GPIO.OUT)
interval = 1

for led in all:
    GPIO.output(led, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(led, GPIO.LOW)

# Write your program above this line
GPIO.cleanup()
