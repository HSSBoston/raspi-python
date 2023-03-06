import blinkt, time

for led in range(4):
    blinkt.set_pixel(led, 255, 255, 255)
blinkt.show()
time.sleep(1)

blinkt.clear()
blinkt.show()

for led in range(4, 8):
    blinkt.set_pixel(led, 255, 255, 255)
blinkt.show()
time.sleep(1)

blinkt.clear()
blinkt.show()
