from gpiozero import MotionSensor
import subprocess, sys, time, kintone, iotutils
from iotutils import getCurrentTimeStamp
# Write your program below

interval = 5
sensor = MotionSensor(21)

while True:
    try:
        sensor.wait_for_motion()
        print("Motion detected: ", end="")

        timeStamp = getCurrentTimeStamp()
        picFile = timeStamp + ".jpg"
        command = "libcamera-still -n -t 500 --width 800 --height 600 -o " + picFile

        status = subprocess.run(command, capture_output=True, shell=True)
        if status.returncode == 0:
            print(timeStamp + " Photo captured.")
        else:
            print("Failed to capture a picture")
            sys.exit()

        time.sleep(interval)
    except KeyboardInterrupt:
        break

