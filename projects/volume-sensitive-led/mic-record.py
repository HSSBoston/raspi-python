import subprocess, wave
from iotutils import getCurrentTimeStamp
import numpy as np
# Write your program below

timeStamp = getCurrentTimeStamp()
fileName = timeStamp + ".wav"
command = "arecord -d 5 -f cd " + fileName
subprocess.run(command, shell=True)

wavFile = wave.open(fileName, "r")
numSamples = wavFile.getnframes()
wavData = wavFile.readframes(numSamples)
wavFile.close()
soundSamples = np.frombuffer(wavData, dtype="int16") / float(2**15)

maxVolLevel = max(soundSamples)
print(maxVolLevel) 
