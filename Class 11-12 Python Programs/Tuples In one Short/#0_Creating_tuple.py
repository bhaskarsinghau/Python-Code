# Tuple are immutable i.e, you cannot changed the element.

# Empty tuple
a = ()       

# Single Element tuple
b = (1)              

# Nested tuple
c = ('a','b','c',(1,2,3),'d')    

# Long tuple
d = (1,2,3,4,5,6,7,8,9,0,3,42,42,24,24,5,6,43,53,3)    

print(set(d)) # Create well defined Collection of d element.  
# Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 42, 43, 53, 24}

# t = tuple(<sequence>)
f = tuple('hello')
print(f)

# Output: ('h', 'e', 'l', 'l', 'o')
# the string become tuple (TypeCasting)
 
g = ['s','c','h','o','o','l'] # type(g): list
h = tuple(g)
print(h)

# Output: ('s', 'c', 'h', 'o', 'o', 'l')
# the list become tuple (TypeCasting)

print('''Written by : Bhaskar Singh
-------- Tuple in One Shot--------------------------------------------


---------Follow on: STARLINK.ATWEBPAGES.COM---------------------------
---------Software - Visual Studio Code - Insider----------------------''')