from iotutils_neopixel import Neopixel
from colorzero import Color, Hue
import time

ledCount = 90
ledPin = 18

strip = Neopixel(ledCount, ledPin)

color = Color("red")

for pixel in range(ledCount):
    degree = pixel * 360/ledCount
    strip.setColor(pixel, color + Hue(deg=degree))
strip.show()
time.sleep(5)

strip.fill(Color("black"))
strip.show()



