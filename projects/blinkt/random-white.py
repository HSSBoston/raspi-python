import blinkt, time, random

while True:
    try:
        blinkt.set_pixel(random.randint(0, 7),
                         255, 255, 255)
        blinkt.show()
        time.sleep(1)
        blinkt.clear()
        blinkt.show()
    except KeyboardInterrupt:
        break

blinkt.clear()
blinkt.show()
