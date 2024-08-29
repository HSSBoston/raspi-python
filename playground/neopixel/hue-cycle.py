from iotutils_neopixel import Neopixel
from colorzero import Color, Hue
import time

ledCount = 90
ledPin = 18

strip = Neopixel(ledCount, ledPin)

strip.fill(Color("red"))
strip.show()

while True:
    try:
        adjustedColor = strip.getColor(0) + Hue(deg=1)
        strip.fill(adjustedColor)
        strip.show()
        time.sleep(0.01)
    except KeyboardInterrupt:
        break

strip.fill(Color("black"))
strip.show()


