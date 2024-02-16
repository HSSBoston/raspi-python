from gpiozero import LED
import time
# Write your program below

onPeriod = 2
offPeriod = 1

redLed = LED(21)

redLed.on()
time.sleep(onPeriod)
redLed.off()
time.sleep(offPeriod)

redLed.on()
time.sleep(onPeriod)
redLed.off()
time.sleep(offPeriod)

redLed.on()
time.sleep(onPeriod)
redLed.off()
