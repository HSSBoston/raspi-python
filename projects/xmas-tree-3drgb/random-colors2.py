from tree import RGBXmasTree
from colorzero import Color, Hue
import time, random
# Write your program below

tree = RGBXmasTree()

starLight = tree.star()
starLight.color = Color("white")

while True:
    try:
        for light in tree.nonStarLights():
            r = random.random()
            g = random.random()
            b = random.random()
            light.color = Color(r, g, b)
    except KeyboardInterrupt:
        break

tree.off()

# Write your program above this line
tree.close()