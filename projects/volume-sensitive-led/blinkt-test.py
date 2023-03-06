from blinkt import set_pixel, set_brightness, show, clear
import time

set_pixel(0, 255, 255, 255)
show()
time.sleep(5)
clear()
show()


# set_pixel(pixel_no, red, green, blue, brightness)
# set_all(red, green, blue, brightness)
# set_brightness(0.5)