from tree import RGBXmasTree
from colorzero import Color
import time
# Write your program below

tree = RGBXmasTree()
interval = 2
starLight = tree.star()

while True:
    try:
        starLight.on()
        time.sleep(interval)
        starLight.off()
        time.sleep(interval)
    except KeyboardInterrupt:
        break

tree.off()

# Write your program above this line
tree.close()