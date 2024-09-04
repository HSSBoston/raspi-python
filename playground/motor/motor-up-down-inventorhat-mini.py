import time
from inventorhatmini import InventorHATMini, MOTOR_A
from ioexpander.common import NORMAL_DIR, REVERSED_DIR

board = InventorHATMini(init_leds=False)
motor = board.motors[MOTOR_A]
motor.enable()

def down(duration):
    motor.direction(REVERSED_DIR)
    motor.speed(0.75)
    time.sleep(duration)
    motor.stop()

def up(duration):
    motor.direction(NORMAL_DIR)
    motor.speed(0.75)
    time.sleep(duration)
    motor.stop()

if __name__ == "__main__":
    down(3)
    time.sleep(1)
    up(3)


