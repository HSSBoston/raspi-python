import RPi.GPIO as GPIO, time
GPIO.setmode(GPIO.BCM)
# Start writing your program below

leftBottom, leftMidBotton, leftMiddle, leftMidTop, leftTop = (18, 17, 16, 13, 24)
rightBottom, rightMidBotton, rightMiddle, rightMidTop, rightTop = (19, 20, 21, 22, 23)
leftEye, rightEye = (12, 6)

left =[leftBottom, leftMidBotton, leftMiddle, leftMidTop, leftTop]
right = [rightBottom, rightMidBotton, rightMiddle, rightMidTop, rightTop]
eyes = [leftEye, rightEye]
all = left + right + eyes

GPIO.setup(all, GPIO.OUT)

GPIO.output(all, GPIO.HIGH)
time.sleep(3)
GPIO.output(all, GPIO.LOW)

# Write your program above this line
GPIO.cleanup()