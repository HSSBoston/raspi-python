import blinkt, time

for led in range(8):
    blinkt.set_pixel(led, 255, 255, 255)
    blinkt.show()
    time.sleep(0.5)

for led in reversed(range(8)):
    blinkt.set_pixel(led, 0, 0, 0)
    blinkt.show()
    time.sleep(0.5)

blinkt.clear()
blinkt.show()
