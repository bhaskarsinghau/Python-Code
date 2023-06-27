# This function returns all the key value pair of dictionary in the form of list of tuples. for example:
A = {1 : "One", 2 : "Two", 3 : "Three"}
B = {'A' : "Apple", 'B' : "Bat", 'C' : "Cat", 'D' : "Doll"}
print(A.items())
print(B.items())

# Output:dict_items([(1, 'One'), (2, 'Two'), (3, 'Three')])
# dict_items([('A', 'Apple'), ('B', 'Bat'), ('C', 'Cat'), ('D', 'Doll')])

'''
@ What is the difference between print(A) and print(A.items( )) Where ‘A’ is dictionary given above.

Ans. There is difference in the output of dictionary as print command print all key-value pair in curly 
braces while items( ) return all key value pairs as a list of tuples. for example
'''
A = {1 : "One", 2 : "Two", 3 : "Three"}
print(A.items())
print(A)

# OUTPUT:dict_items([(1, 'One'), (2, 'Two'), (3, 'Three')])
# {1: 'One', 2: 'Two', 3: 'Three'}

# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com