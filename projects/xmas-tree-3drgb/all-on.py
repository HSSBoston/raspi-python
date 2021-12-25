from tree import RGBXmasTree
from colorzero import Color
import time
# Write your program below

tree = RGBXmasTree()

while True:
    try:
        tree.on()
        time.sleep(1)
    except KeyboardInterrupt:
        break

tree.off()

# Write your program above this line
tree.close()
