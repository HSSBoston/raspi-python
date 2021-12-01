import os, sys, kintone, time
from kintone import getCurrentTimeStamp
# Write your program below

timeStamp = getCurrentTimeStamp()
videoFile = timeStamp + ".h264"
command1 = "raspivid -t 3000 -w 640 -h 480 -fps 15 -o " + videoFile
status = os.system(command1)

if(status==0):
    print(timeStamp, end=" ")
    print("Video captured.")
    mp4File = timeStamp + ".mp4"
    command2 = "MP4Box -quiet -fps 15 -add " + videoFile + " " + mp4File
    os.system(command2)
    command3 = "rm " + videoFile
    os.system(command3)
else:
    print("Failed to capture a video.")
    sys.exit()
