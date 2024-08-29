from iotutils_neopixel import Neopixel
from colorzero import Color, Hue
import time

ledCount = 10
ledPin = 18
interval = 0.5
neop = Neopixel(ledCount, ledPin)

for led in range(ledCount):
    neop.setRGB(led, (255, 0, 0))
    neop.show()
    time.sleep(interval)

for led in reversed(range(ledCount)):
    neop.setColor(led, Color("yellow"))
    neop.show()
    time.sleep(interval)

neop.fillRGB((0, 0, 0))
neop.show()