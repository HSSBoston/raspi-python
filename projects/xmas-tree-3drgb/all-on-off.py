from tree import RGBXmasTree
from colorzero import Color
import time
# Write your program below

tree = RGBXmasTree()
interval = 2

while True:
    try:
        tree.on()
        time.sleep(interval)
        tree.off()
        time.sleep(interval)
    except KeyboardInterrupt:
        break

tree.off()

# Write your program above this line
tree.close()