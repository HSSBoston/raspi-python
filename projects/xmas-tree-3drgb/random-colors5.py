from tree import RGBXmasTree
from colorzero import Color, Hue
import time, random
# Write your program below

tree = RGBXmasTree()
colors = [Color("red"), Color("green"), Color("blue")]

starLight = tree.star()
starLight.color = Color("white")

for light in tree.nonStarLights():
    light.color = random.choice(colors)

while True:
    try:
        light = random.choice(tree.nonStarLights())
        randomDegree = random.random()*360
        light.color = light.color + Hue(deg=randomDegree)
        light.lightness = random.random()
    except KeyboardInterrupt:
        break

tree.off()

# Write your program above this line
tree.close()