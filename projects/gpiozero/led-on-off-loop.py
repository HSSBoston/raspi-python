from gpiozero import LED
import time
# Write your program below

onPeriod = 2
offPeriod = 1

redLed = LED(21)
blueLed = LED(14)

for x in range(3):
    redLed.on()
    time.sleep(onPeriod)
    redLed.off()
    time.sleep(offPeriod)
    blueLed.on()
    time.sleep(onPeriod)
    blueLed.off()
    time.sleep(offPeriod)