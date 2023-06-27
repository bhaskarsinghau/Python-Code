#We can easily add new element in dictionary by the following way:

A = {1 : "One", 2 : "Two", 3 : "Three"} 
A[4] = "Four"
print(A)

# OUTPUT: {1 : "One", 2 : "Two", 3 : "Three", 4 : "Four"}

'''
We can also join two dictionaries into one by using update() method.
It merge the keys and values of one dictionary into other and overwrites the values of the same key.
'''
A = {1 : "One", 2 : "Two", 3 : "Three"}
B = {1: 'Amit', 2: 'Sunil', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
A.update(B)
print(A)

# OUTPUT: {1: 'Amit', 2: 'Sunil', 3: 'Three', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
#It over writes the values of same keys and add the values of different keys.

# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com