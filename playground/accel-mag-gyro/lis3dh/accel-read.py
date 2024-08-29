import time
from lis3dh import LIS3DH

sensor = LIS3DH()

while True:
    try:
        x, y, z = sensor.readG()
        print(x, y, z)
        time.sleep(0.5)
    except KeyboardInterrupt:
        break
