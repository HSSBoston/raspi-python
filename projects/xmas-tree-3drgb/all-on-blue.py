from tree import RGBXmasTree
from colorzero import Color
import time
# Write your program below

tree = RGBXmasTree()
tree.color = Color("blue")
time.sleep(3)
tree.off()

# Write your program above this line
tree.close()
