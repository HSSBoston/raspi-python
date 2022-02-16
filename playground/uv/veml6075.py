import time
from board import *
from adafruit_veml6075 import VEML6075

i2c = I2C()
uvSensor = VEML6075(i2c)
interval = 3

while True:
    try:
        uvi = uvSensor.uv_index
        print("UV Index: " + str(uvi))        
        time.sleep(interval)
    except KeyboardInterrupt:
        break
