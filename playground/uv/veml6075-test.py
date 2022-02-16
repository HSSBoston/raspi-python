import time
from board import *
from adafruit_veml6075 import VEML6075

#i2c = busio.I2C(board.SCL, board.SDA) # returns busio.I2C
#i2c = busio.I2C(SCL, SDA) #returns busio.I2C
#i2c = board.I2C() # returns busio.I2C
i2c = I2C() # uses board.SCL and board.SDA, and returns busio.I2C

uvSensor = VEML6075(i2c)

while True:
    try: 
        print(uvSensor.uv_index, end=", ")
        print(uvSensor.uva, end=", ")
        print(uvSensor.uvb)
        
        time.sleep(3)
    except KeyboardInterrupt:
        break
