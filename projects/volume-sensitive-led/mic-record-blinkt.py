import subprocess, wave
import numpy as np
from blinkt import set_pixel, set_brightness, show, clear
import time

while True:
    try:
        fileName = "mic-sound.wav"
        command = "arecord -d 1 -f cd " + fileName
        subprocess.run(command, shell=True)

        wavFile = wave.open(fileName, "r")
        numSamples = wavFile.getnframes()
        wavData = wavFile.readframes(numSamples)
        wavFile.close()
        soundSamples = np.frombuffer(wavData, dtype="int16") / float(2**15)

        maxVolLevel = max(soundSamples)
        print(maxVolLevel)
        
        clear()
        show()
        if maxVolLevel >= 0 and maxVolLevel <= 0.125:
            set_pixel(0,255,255,255)
        if maxVolLevel > 0.125 and maxVolLevel <= 0.25:
            set_pixel(1,145,94,253)
            set_pixel(0,145,94,253)
        if maxVolLevel > 0.25 and maxVolLevel <= 0.375:
            set_pixel(2, 1, 103, 251)
            set_pixel(1,1, 103, 251)
            set_pixel(0, 1,103,251)
        if maxVolLevel > 0.375 and maxVolLevel <= 0.5:
            set_pixel(3, 5, 216, 250)
            set_pixel(2, 5, 216, 250)
            set_pixel(1, 5, 216, 250 )
            set_pixel(0,5, 216, 250)
        if maxVolLevel > 0.5 and maxVolLevel <= 0.625:
            set_pixel(4, 5, 239, 4)
            set_pixel(3,  5, 239, 4)
            set_pixel(2, 5, 239, 4)
            set_pixel(1, 5, 239, 4)
            set_pixel(0,5, 239, 4)
        if maxVolLevel > 0.625 and maxVolLevel <= 0.75:
            set_pixel(5, 255, 253, 0)
            set_pixel(4, 255, 253, 0)
            set_pixel(3,  255, 253, 0)
            set_pixel(2, 255, 253, 0)
            set_pixel(1, 255, 253, 0)
            set_pixel(0,255, 253, 0)
        if maxVolLevel > 0.75 and maxVolLevel <= 0.875:
            set_pixel(6, 253, 110, 9)
            set_pixel(5,253, 110,9)
            set_pixel(4,253, 110,9)
            set_pixel(3,253, 110,9)
            set_pixel(2,253, 110,9)
            set_pixel(1, 253, 110,9)
            set_pixel(0,253, 110,9)
        if maxVolLevel > 0.875 and maxVolLevel <= 1:
            set_pixel(7, 255, 0, 0)
            set_pixel(6, 255, 0, 0)
            set_pixel(5, 255, 0, 0)
            set_pixel(4, 255, 0, 0)
            set_pixel(3, 255, 0, 0)
            set_pixel(2, 255, 0, 0)
            set_pixel(1,  255, 0, 0)
            set_pixel(0, 255, 0, 0)
            
        show()
        time.sleep(0.1)

    except KeyboardInterrupt:
        break
        

    

        
    