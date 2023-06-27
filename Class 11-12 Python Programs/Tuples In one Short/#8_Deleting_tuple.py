# The individual element of tuple cannot be deleted.
# because tuple are immutable 

# But you can delete a complete tuple with a del statement.

a = (1,2,3,4,5,6,7)
print(a)   # Output: (1, 2, 3, 4, 5, 6, 7)

del(a)
print(a)

'''
    print(a)
NameError: name 'a' is not defined
'''

# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com