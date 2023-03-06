from blinkt import set_pixel, set_brightness, show, clear
import time, subprocess, wave, numpy as np
# Write your program below

fileName = "sound.wav"
duration = 1
command = "arecord -d " + str(duration) + " -f cd " + fileName

while True:
    try:
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
        if maxVolLevel < 0.05:
            set_pixel(0, 255, 255, 255)
            show()
        if maxVolLevel >= 0.05 and maxVolLevel < 1:
            set_pixel(0, 255, 255, 255)
            set_pixel(1, 255, 122, 122)
            show()

        time.sleep(0.1)
        
    except KeyboardInterrupt:
        clear()
        show()
        break




# set_pixel(pixel_no, red, green, blue, brightness)
# set_all(red, green, blue, brightness)
# set_brightness(0.5)
