#index() returns the lowest index of string
a = ("it goes as - ringa ringa roses")
b = (a.index('ringa'))
print(b)
# Output: 13

#a.count('str',start,stop)
a = ("it goes as - ringa ringa roses")
b = (a.index('ringa',15,25))
print(b)
# Output: 19

#it works like find(), but find() returns -1 if str is not found,
#But index() raises an exception (Value Error: substring not found)

a = ("it goes as - ringa ringa roses")
b = (a.index('x'))
print(b)

# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com
