import RPi.GPIO as GPIO, subprocess, sys, time, kintone, iotutils
from iotutils import getCurrentTimeStamp
GPIO.setmode(GPIO.BCM)
# Write your program below

sdomain = "SUB-DOMAIN-NAME"
appId = "APP-ID-NUMBER"
token = "APP-TOKEN"

motionPin = 21
GPIO.setup(motionPin, GPIO.IN)
interval = 5

while True:
    try:
        if GPIO.input(motionPin) == GPIO.HIGH:
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
