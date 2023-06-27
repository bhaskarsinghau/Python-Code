x = "-"
y = x*10
print(y,"Using Tuple Unpacking",y)

a = (1,2,3,4)
print("Original tuple",a)
a,b,c,d = a
c = 77
a = (a,b,c,d)
print("Modified tuple",a)

''' Output:  ---------- Using Tuple Unpacking ----------
Original tuple (1, 2, 3, 4)
Modified tuple (1, 2, 77, 4)
'''

'''
a = (1,2,3,4)

# First Unpack
a,b,c,d = a

# Change desired variables you want
c = 77

#Repack again
a = (a,b,c,d)
print(a)

'''
print()

# Using the constructor functions of list and tuples.
x = "-"
y = x*8
print(y,"Using Constructor functions",y)

a = (1,2,3,4) 
print("Original tuple",a)
b = list(a)
c = b[0]='Bhaskar'
d = tuple(b)
print("Modified tuple",d)

''' Output: -------- Using Constructor functions --------
Original tuple (1, 2, 3, 4)
Modified tuple ('Bhaskar', 2, 3, 4) '''

# Concept: Enter the tuple.
# then change the tuple into list through typecasting.
# Now edit the list with the help of its index.
# then change the list into tuple through typecasting.
# And Print your result.

# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com