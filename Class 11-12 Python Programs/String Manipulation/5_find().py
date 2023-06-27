#find() returns the lowest index of string
a = ("it goes as - ringa ringa roses")
b = (a.find('ringa'))
print(b)
# Output: 13

#If it not found it give output as -1
a = ("it goes as - ringa ringa roses")
b = (a.find('x'))
print(b)
# Output: -1

#a.count('str',start,stop)
a = ("it goes as - ringa ringa roses")
b = (a.find('ringa',15,25))
print(b)
# Output: 19
