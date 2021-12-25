from tree import RGBXmasTree
from colorzero import Color, Hue
import time
# Write your program below

tree = RGBXmasTree()
tree.color = Color('red')

while True:
    try:
        tree.color += Hue(deg=1)
    except KeyboardInterrupt:
        break
    
tree.off()

# Write your program above this line
tree.close()