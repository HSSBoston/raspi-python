import os, sys, kintone, time
from kintone import getCurrentTimeStamp
# Write your program below

sdomain = "SUB-DOMAIN-NAME"
appId = "APP-ID-NUMBER"
token = "APP-TOKEN"

interval = 3

while True: 
    try:
        timeStamp = getCurrentTimeStamp()
        videoFile = timeStamp + ".h264"
        command1 = "raspivid -w 640 -h 480 -o " + videoFile
        status = os.system(command1)

        if(status==0):
            print(timeStamp, end=" ")
            print("Video captured.")
            mp4File = timeStamp + ".mp4"
            command2 = "MP4Box -quiet -add " + videoFile + " " + mp4File
            os.system(command2)
            command3 = "rm " + videoFile
            os.system(command3)
        else:
            print("Failed to capture a video.")
            sys.exit()
            
        fileKey = kintone.uploadFile(subDomain=sdomain,
                                     apiToken=token,
                                     filePath=mp4File)
        if fileKey is None:
            sys.exit()

        memo = "Hi from Raspi! (MP4 Video)"
        payload = {"app": appId,
                   "record": {"photo": {"value": [{"fileKey": fileKey}] },
                              "memo": {"value": memo} }}

        recordId = kintone.uploadRecord(subDomain=sdomain,
                                        apiToken=token,
                                        record=payload)
        if recordId is None:
            sys.exit()
        time.sleep(interval)
    except KeyboardInterrupt:
        break

