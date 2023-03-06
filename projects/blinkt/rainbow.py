import blinkt, time

blinkt.set_pixel(0, 255, 0, 0)
blinkt.set_pixel(1, 255, 191, 41)
blinkt.set_pixel(2, 128, 255, 0)
blinkt.set_pixel(3, 0, 255, 64)
blinkt.set_pixel(4, 0, 255, 255)
blinkt.set_pixel(5, 0, 64, 255)
blinkt.set_pixel(6, 128, 0, 255)
blinkt.set_pixel(7, 255, 0, 191)

blinkt.show()
time.sleep(2)

blinkt.clear()
blinkt.show()
