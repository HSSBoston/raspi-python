import RPi.GPIO as GPIO, os, sys, kintone, time
from kintone import getCurrentTimeStamp
GPIO.setmode(GPIO.BCM)
# Start writing your program below

motionPin = 21
GPIO.setup(motionPin, GPIO.IN)
interval = 5

#sdomain = "SUB-DOMAIN-NAME"
#appId = "APP-ID-NUMBER"
#token = "APP-TOKEN"

while True:
    try:
        if GPIO.input(motionPin) == GPIO.HIGH:
            print("Motion detected: ", end="")
            
            timeStamp = getCurrentTimeStamp()
            picFile = timeStamp + ".jpg"
            command = "raspistill -t 500 -w 800 -h 600 -o " + picFile

            status = os.system(command)
            if(status==0):
                print(timeStamp, end=" ")
                print("Photo captured.")
            else:
                print("Failed to capture a picture")
                sys.exit()

            fileKey = kintone.uploadFile(subDomain=sdomain,
                                         apiToken=token,
                                         filePath=picFile)
            if fileKey is None:
                sys.exit()

            memo = "Motion detected"
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

# Write your program above this line
GPIO.cleanup()
