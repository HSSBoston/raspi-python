from tree import RGBXmasTree
from colorzero import Color, Hue
import time, random
# Write your program below

colors = [Color("red"), Color("green"), Color("blue"),
          Color("magenta"), Color("cyan"), Color("yellow")]

tree = RGBXmasTree()
starLight = tree.star()
starLight.color = Color("gray")

for light in tree.nonStarLights():
    light.color = random.choice(colors)

while True:
    try:
        for light in tree.nonStarLights():
            light.color = light.color + Hue(deg=45)
    except KeyboardInterrupt:
        break

tree.off()

# Write your program above this line
tree.close()