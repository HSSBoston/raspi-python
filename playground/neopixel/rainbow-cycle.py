from iotutils_neopixel import Neopixel
from colorzero import Color, Hue
import time

ledCount = 90
ledPin = 18

strip = Neopixel(ledCount, ledPin)

firstLedColor = Color("red")

while True:
    try:
        for pixel in range(ledCount):
            degree = pixel * 360/ledCount
            strip.setColor(pixel, firstLedColor + Hue(deg=degree))
        strip.show()
        time.sleep(0.1)
        firstLedColor = firstLedColor + Hue(deg=degree)
    except KeyboardInterrupt:
        break
    
strip.fill(Color("black"))
strip.show()



