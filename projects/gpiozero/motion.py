from gpiozero import MotionSensor
import subprocess, sys, time, kintone, iotutils
from iotutils import getCurrentTimeStamp
# Write your program below

interval = 5
sensor = MotionSensor(21)

while True:
    try:
        sensor.wait_for_motion()
        print("Motion detected: " + getCurrentTimeStamp())
        time.sleep(interval)
    except KeyboardInterrupt:
        break
