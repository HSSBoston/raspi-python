from tree import RGBXmasTree
from colorzero import Color
import time
# Write your program below

tree = RGBXmasTree()
interval = 2

while True:
    try:
        for light in tree:
            light.color = Color("green")
            time.sleep(interval)
            light.off()
    except KeyboardInterrupt:
        break

tree.off()

# Write your program above this line
tree.close()