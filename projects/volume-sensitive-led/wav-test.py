import wave
from soundanalysis import wavToSamples

wavFileName = "mic-sound.wav"

# wavFile = wave.open(wavFileName, mode="rb")
# # Since the recorded sound is formatted in CD quality (with "-f cd"
# # option for the arecord command), sampwidth==2 (bytes), dtype=="int16". 
# print("Reading " + wavFileName + ": " + str(wavFile.getparams()))
# sampleWidth = wavFile.getsampwidth()

soundSamples = wavToSamples(wavFileName)

maxVolLevel = max(soundSamples)
print(maxVolLevel)
