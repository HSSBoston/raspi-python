from iotutils_neopixel import Neopixel
from colorzero import Color, Hue
import time

ledCount = 10
ledPin = 18
neop = Neopixel(ledCount, ledPin)

neop.fillRGB((255, 0, 0))
neop.show()
time.sleep(3)

neop.fillRGB((0, 0, 0))
neop.show()

