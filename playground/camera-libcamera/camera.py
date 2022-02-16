import subprocess, sys, time, kintone, iotutils
from iotutils import getCurrentTimeStamp
# Write your program below

timeStamp = getCurrentTimeStamp()
picFile = timeStamp + ".jpg"
command = "libcamera-still -n -t 500 --width 800 --height 600 -o " + picFile

subprocess.run(command, shell=True)