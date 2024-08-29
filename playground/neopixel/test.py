from iotutils_neopixel import LedStrip
from colorzero import Color, Hue
import time

ledCount = 90
ledPin = 18

strip = LedStrip(ledCount, ledPin)

strip.setColor(0, Color("yellow"))
strip.show()
print( strip.getRGB(0) )
print( strip.getColor(0) )
time.sleep(2)

strip.setRGB(0, (0, 255, 0))
strip.show()
print( strip.getRGB(0) )
print( strip.getColor(0) )
time.sleep(2)

strip.fill(Color("red"))
print( strip.getRGB(0) )
print( strip.getColor(0) )
strip.show()
time.sleep(2)

strip.fillRGB( (0, 0, 255) )
strip.changeBrightness(0.75)
print( strip.getRGB(0) )
print( strip.getColor(0) )
strip.show()
time.sleep(2)

strip.fill(Color("black"))
strip.show()
