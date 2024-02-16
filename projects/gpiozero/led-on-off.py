from gpiozero import LED
import time
# Write your program below

redLed = LED(21)

redLed.on()
time.sleep(3)
redLed.off()
