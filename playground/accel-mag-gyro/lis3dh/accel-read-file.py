import csv, time
from iotutils import getCurrentTimeStamp
from lis3dh import LIS3DH

sensor = LIS3DH()
accelData = []

while True:
    try:
        x, y, z = sensor.readG()
        currentTime = time.time()
        accelData.append([currentTime, x, y, z])
        time.sleep(0.01)
    except KeyboardInterrupt:
        break

timeStamp = getCurrentTimeStamp()
fileName = "accel-" + timeStamp + ".csv"

with open(fileName, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["utime (s)", "X (G)", "Y (G)", "Z (G)"])
    writer.writerows(accelData)
print(fileName + " saved.")
