from tree import RGBXmasTree
from colorzero import Color, Hue
import time, random
# Write your program below

tree = RGBXmasTree()
degree = 30

starLight = tree.star()
starLight.color = Color("white")

for light in tree.nonStarLights():
    r = random.random()
    g = random.random()
    b = random.random()
    light.color = Color(r, g, b)

while True:
    try:
        for light in tree.nonStarLights():
            light.color = light.color + Hue(deg=degree)
    except KeyboardInterrupt:
        break

tree.off()

# Write your program above this line
tree.close()