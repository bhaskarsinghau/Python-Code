import random
import math

fnum = random.random() * (95-45)+45
inum = math.ceil(fnum)
print("Random number between 45...95: ",fnum)
print("Nearest higher integer: ",inum)