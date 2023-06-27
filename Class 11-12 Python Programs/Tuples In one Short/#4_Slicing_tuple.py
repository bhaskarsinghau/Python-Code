# Slicing the tuple
# seq = l[start:stop-1:step]

tuple = (10,12,14,20,22,24,30,32,34)

print(tuple[0:10:2])  # Output: (10, 14, 22, 30, 34)
print(tuple[::3])     # Output: (10, 20, 30)
print(tuple[3:-3])    # Output: (20, 22, 24)

b = tuple[2:5] * 3
print("tuple[2:5] * 3 :",b)

# Output: tuple[2:5] * 3 : (14, 20, 22, 14, 20, 22, 14, 20, 22)

c = tuple[2:5] + (3,4)
print("tuple[2:5] + (3,4) :",c)

# Output: tuple[2:5] + (3,4) : (14, 20, 22, 3, 4)

# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com
