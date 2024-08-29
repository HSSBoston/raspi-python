from colorzero import Color, Hue
import time

c = Color("red")
print(c)
print(c.hue)

while True:
    try:
        adjustedColor = c + Hue(deg=10)
        c = adjustedColor
        print(c)
        time.sleep(1)
    except KeyboardInterrupt:
        break



